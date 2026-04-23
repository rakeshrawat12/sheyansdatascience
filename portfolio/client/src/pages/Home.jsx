import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

const Home = () => {
  const [typedText, setTypedText] = useState('')
  const texts = ['Data Scientist', 'ML Engineer', 'Data Analyst', 'AI Enthusiast']
  const [textIndex, setTextIndex] = useState(0)
  const [charIndex, setCharIndex] = useState(0)
  const [isDeleting, setIsDeleting] = useState(false)

  useEffect(() => {
    const typingSpeed = isDeleting ? 50 : 100
    const pauseDuration = 2000

    const timer = setTimeout(() => {
      if (!isDeleting && charIndex <= texts[textIndex].length) {
        setTypedText(texts[textIndex].substring(0, charIndex))
        setCharIndex(prev => prev + 1)
      } else if (isDeleting && charIndex >= 0) {
        setTypedText(texts[textIndex].substring(0, charIndex))
        setCharIndex(prev => prev - 1)
      } else if (charIndex === texts[textIndex].length + 1) {
        setIsDeleting(true)
        setTimeout(() => {}, pauseDuration)
      } else if (isDeleting && charIndex === 0) {
        setIsDeleting(false)
        setTextIndex(prev => (prev + 1) % texts.length)
      }
    }, typingSpeed)

    return () => clearTimeout(timer)
  }, [charIndex, isDeleting, textIndex])

  return (
    <section className="section hero" id="home">
      <div className="hero-content">
        <p className="intro">Hi, my name is</p>
        <h1>Rakesh Singh Rawat.</h1>
        <h2>I build things with data.</h2>
        <h3>
          I'm a <span className="typing-text">{typedText}</span>
          <span className="cursor"></span>
        </h3>
        <p>
          A passionate Data Scientist specializing in machine learning, statistical analysis,
          and turning complex data into actionable insights. Let's explore my work together.
        </p>
        <div className="hero-btns">
          <Link to="/projects" className="btn btn-filled">
            View My Projects <span className="btn-icon">→</span>
          </Link>
          <Link to="/contact" className="btn">
            Get In Touch <span className="btn-icon">↗</span>
          </Link>
        </div>
      </div>
    </section>
  )
}

export default Home
