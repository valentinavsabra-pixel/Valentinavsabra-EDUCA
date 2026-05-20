import { create } from 'zustand'

interface User {
  id: string
  email: string
  name: string
  type: 'student' | 'teacher'
  avatar?: string
  xp?: number
  level?: number
}

interface AuthStore {
  user: User | null
  isAuthenticated: boolean
  login: (email: string, password: string) => Promise<void>
  signup: (name: string, email: string, password: string, type: 'student' | 'teacher') => Promise<void>
  logout: () => void
  setUser: (user: User | null) => void
}

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  isAuthenticated: false,
  login: async (email, password) => {
    const mockUser: User = {
      id: '1',
      email,
      name: 'Usuário',
      type: 'student',
      xp: 0,
      level: 1,
    }
    set({ user: mockUser, isAuthenticated: true })
  },
  signup: async (name, email, password, type) => {
    const mockUser: User = {
      id: '1',
      email,
      name,
      type,
      xp: 0,
      level: 1,
    }
    set({ user: mockUser, isAuthenticated: true })
  },
  logout: () => {
    set({ user: null, isAuthenticated: false })
  },
  setUser: (user) => {
    set({ user, isAuthenticated: !!user })
  },
}))

interface StudentStore {
  xp: number
  level: number
  medals: string[]
  streak: number
  addXP: (amount: number) => void
  addMedal: (medal: string) => void
  incrementStreak: () => void
  resetStreak: () => void
}

export const useStudentStore = create<StudentStore>((set) => ({
  xp: 0,
  level: 1,
  medals: [],
  streak: 0,
  addXP: (amount) =>
    set((state) => ({
      xp: state.xp + amount,
      level: Math.floor((state.xp + amount) / 1000) + 1,
    })),
  addMedal: (medal) =>
    set((state) => ({
      medals: [...state.medals, medal],
    })),
  incrementStreak: () =>
    set((state) => ({
      streak: state.streak + 1,
    })),
  resetStreak: () =>
    set({ streak: 0 }),
}))