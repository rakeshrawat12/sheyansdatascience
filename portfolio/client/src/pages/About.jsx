import { useEffect, useRef } from 'react'

const About = () => {
  const skillRefs = useRef([])

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible')
          }
        })
      },
      { threshold: 0.5 }
    )

    skillRefs.current.forEach((ref) => {
      if (ref) observer.observe(ref)
    })

    return () => observer.disconnect()
  }, [])

  return (
    <section className="section" id="about">
      <div className="container">
        <h2 className="section-title" data-number="02.">
          About Me
        </h2>
        <div className="about-content">
          <div className="about-text">
            <p>
              Hello! I'm <strong style={{ color: 'var(--light)' }}>Rakesh Singh Rawat</strong>, a
              dedicated <strong style={{ color: 'var(--primary)' }}>Data Scientist</strong> with a
              strong foundation in statistical modeling, machine learning, and data analysis.
              I specialize in transforming complex datasets into actionable insights that drive
              business decisions.
            </p>
            <p>
              My journey in data science has led me to work on diverse projects ranging from
              predictive analytics to natural language processing. I believe in the power of
              data to drive meaningful decisions and solve real-world problems.
            </p>
            <p>Here are a few technologies I've been working with recently:</p>
            <ul className="tech-list">
              <li><span style={{ color: 'var(--primary)' }}>Python</span> — Data Analysis & ML</li>
              <li><span style={{ color: 'var(--primary)' }}>Machine Learning</span> — TensorFlow, PyTorch</li>
              <li><span style={{ color: 'var(--primary)' }}>Data Visualization</span> — Tableau, Plotly</li>
              <li><span style={{ color: 'var(--primary)' }}>Databases</span> — SQL, MongoDB, PostgreSQL</li>
              <li><span style={{ color: 'var(--primary)' }}>Cloud Platforms</span> — AWS, GCP</li>
            </ul>
          </div>
          <div className="about-image">
            <div className="avatar-placeholder">
              <span style={{ fontSize: '3rem', marginBottom: '10px' }}>👨‍💻</span>
              <span>RSR</span>
            </div>
          </div>
        </div>

        <div className="stats-grid">
          <div className="stat-card" ref={(el) => skillRefs.current[0] = el}>
            <h4>2+</h4>
            <p>Years Experience</p>
          </div>
          <div className="stat-card" ref={(el) => skillRefs.current[1] = el}>
            <h4>10+</h4>
            <p>Projects Completed</p>
          </div>
          <div className="stat-card" ref={(el) => skillRefs.current[2] = el}>
            <h4>5+</h4>
            <p>ML Models Deployed</p>
          </div>
        </div>
      </div>
    </section>
  )
}

export default About
