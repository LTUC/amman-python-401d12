"use client";
import './globals.css'
import Header from "./components/Header"
import ThemeWrapper from './context/theme';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <ThemeWrapper>
          <Header />
          <main>{children}</main>
        </ThemeWrapper>
      </body>
    </html>
  )
}