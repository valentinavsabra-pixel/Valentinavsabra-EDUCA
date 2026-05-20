import './globals.css'
import type { Metadata } from 'next'
import { Toaster } from 'react-hot-toast'

export const metadata: Metadata = {
  title: 'Educa - Plataforma Educacional Gamificada',
  description: 'Plataforma educacional moderna, interativa e gratuita com gamificação, trilhas de aprendizagem e assistentes de IA.',
  keywords: 'educação, aprendizagem, gamificação, estudantes, professores',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body>
        {children}
        <Toaster position="top-right" />
      </body>
    </html>
  )
}