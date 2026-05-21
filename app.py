from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Simulação de banco de dados em memória
users_db = {
    'aluno@educa.com': {
        'password': generate_password_hash('123456'),
        'name': 'Aluno Teste',
        'type': 'student',
        'xp': 250,
        'level': 2
    },
    'professor@educa.com': {
        'password': generate_password_hash('123456'),
        'name': 'Professor Teste',
        'type': 'teacher',
        'xp': 500,
        'level': 3
    }
}

disciplines = {
    'portugues': {
        'name': 'Português',
        'icon': '📚',
        'progress': 80,
        'lessons': 12,
        'completed': 10
    },
    'matematica': {
        'name': 'Matemática',
        'icon': '🔢',
        'progress': 60,
        'lessons': 15,
        'completed': 9
    },
    'ingles': {
        'name': 'Inglês',
        'icon': '🌍',
        'progress': 40,
        'lessons': 10,
        'completed': 4
    },
    'historia': {
        'name': 'História',
        'icon': '📖',
        'progress': 75,
        'lessons': 8,
        'completed': 6
    }
}

achievements = [
    {'id': 1, 'name': 'Iniciante', 'icon': '🥇', 'xp': 100, 'unlocked': True},
    {'id': 2, 'name': 'Aprendiz', 'icon': '🥈', 'xp': 500, 'unlocked': True},
    {'id': 3, 'name': 'Mestre', 'icon': '🥉', 'xp': 1000, 'unlocked': False},
    {'id': 4, 'name': 'Campeão', 'icon': '👑', 'xp': 5000, 'unlocked': False},
]

questions = {
    'portugues': [
        {
            'id': 1,
            'question': 'Qual é o sinônimo de "felicidade"?',
            'options': ['Tristeza', 'Alegria', 'Raiva', 'Medo'],
            'correct': 1,
            'difficulty': 'easy'
        },
        {
            'id': 2,
            'question': 'Em que século Camões escreveu "Os Lusíadas"?',
            'options': ['XV', 'XVI', 'XVII', 'XVIII'],
            'correct': 1,
            'difficulty': 'medium'
        }
    ],
    'matematica': [
        {
            'id': 1,
            'question': 'Quanto é 15 + 27?',
            'options': ['40', '42', '35', '45'],
            'correct': 1,
            'difficulty': 'easy'
        },
        {
            'id': 2,
            'question': 'Qual é a raiz quadrada de 144?',
            'options': ['10', '11', '12', '13'],
            'correct': 2,
            'difficulty': 'medium'
        }
    ]
}

@app.route('/')
def index():
    """Homepage"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de Login"""
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        user = users_db.get(email)
        if user and check_password_hash(user['password'], password):
            session['user_email'] = email
            session['user_name'] = user['name']
            session['user_type'] = user['type']
            
            if user['type'] == 'student':
                return jsonify({'success': True, 'redirect': '/student/dashboard'})
            else:
                return jsonify({'success': True, 'redirect': '/teacher/dashboard'})
        
        return jsonify({'success': False, 'error': 'Email ou senha inválidos'}), 401
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Página de Cadastro"""
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        user_type = data.get('type')
        
        if email in users_db:
            return jsonify({'success': False, 'error': 'Email já cadastrado'}), 400
        
        users_db[email] = {
            'password': generate_password_hash(password),
            'name': name,
            'type': user_type,
            'xp': 0,
            'level': 1
        }
        
        session['user_email'] = email
        session['user_name'] = name
        session['user_type'] = user_type
        
        if user_type == 'student':
            return jsonify({'success': True, 'redirect': '/student/dashboard'})
        else:
            return jsonify({'success': True, 'redirect': '/teacher/dashboard'})
    
    return render_template('signup.html')

@app.route('/student/dashboard')
def student_dashboard():
    """Dashboard do Aluno"""
    if 'user_email' not in session or session.get('user_type') != 'student':
        return redirect(url_for('login'))
    
    user = users_db.get(session['user_email'])
    return render_template('student_dashboard.html', 
                         user_name=session['user_name'],
                         xp=user['xp'],
                         level=user['level'],
                         disciplines=disciplines,
                         achievements=achievements)

@app.route('/teacher/dashboard')
def teacher_dashboard():
    """Dashboard do Professor"""
    if 'user_email' not in session or session.get('user_type') != 'teacher':
        return redirect(url_for('login'))
    
    user = users_db.get(session['user_email'])
    return render_template('teacher_dashboard.html',
                         user_name=session['user_name'],
                         xp=user['xp'],
                         level=user['level'],
                         disciplines=disciplines)

@app.route('/quiz/<discipline>', methods=['GET', 'POST'])
def quiz(discipline):
    """Página de Quiz"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        data = request.get_json()
        answer = data.get('answer')
        question_id = data.get('question_id')
        
        disc_questions = questions.get(discipline, [])
        question = next((q for q in disc_questions if q['id'] == question_id), None)
        
        if question:
            is_correct = answer == question['correct']
            xp_reward = 10 if question['difficulty'] == 'easy' else 20 if question['difficulty'] == 'medium' else 30
            
            if is_correct:
                user = users_db[session['user_email']]
                user['xp'] += xp_reward
                user['level'] = (user['xp'] // 500) + 1
            
            return jsonify({
                'correct': is_correct,
                'xp_reward': xp_reward if is_correct else 0,
                'explanation': 'Parabéns! Resposta correta!' if is_correct else 'Tente novamente!'
            })
    
    disc_questions = questions.get(discipline, [])
    return render_template('quiz.html',
                         discipline=discipline,
                         questions=disc_questions,
                         user_name=session['user_name'])

@app.route('/api/questions/<discipline>')
def get_questions(discipline):
    """API para obter questões"""
    if 'user_email' not in session:
        return jsonify({'error': 'Não autenticado'}), 401
    
    disc_questions = questions.get(discipline, [])
    return jsonify(disc_questions)

@app.route('/api/user')
def get_user():
    """API para obter dados do usuário"""
    if 'user_email' not in session:
        return jsonify({'error': 'Não autenticado'}), 401
    
    user = users_db.get(session['user_email'])
    return jsonify({
        'email': session['user_email'],
        'name': session['user_name'],
        'type': session['user_type'],
        'xp': user['xp'],
        'level': user['level']
    })

@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    """Página de Perfil"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    user = users_db.get(session['user_email'])
    return render_template('profile.html',
                         email=session['user_email'],
                         name=session['user_name'],
                         user_type=session['user_type'],
                         xp=user['xp'],
                         level=user['level'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
