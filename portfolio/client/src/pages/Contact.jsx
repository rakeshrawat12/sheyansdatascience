import { useState } from 'react'

const Contact = () => {
  const [formData, setFormData] = useState({ name: '', email: '', message: '' })
  const [status, setStatus] = useState({ type: '', message: '' })
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setStatus({ type: '', message: '' })

    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      })

      if (response.ok) {
        setStatus({
          type: 'success',
          message: '✓ Message sent successfully! I will get back to you soon.'
        })
        setFormData({ name: '', email: '', message: '' })
      } else {
        throw new Error('Failed to send message')
      }
    } catch (error) {
      setStatus({
        type: 'error',
        message: '✗ Failed to send message. Please try again later.'
      })
    } finally {
      setLoading(false)
    }
  }

  return (
    <section className="section" id="contact">
      <div className="container">
        <h2 className="section-title" data-number="05.">
          Get In Touch
        </h2>
        <div className="contact-content">
          <div className="contact-info">
            <h3>Let's Talk</h3>
            <p>
              I'm always open to discussing new projects, creative ideas, or opportunities
              to be part of your data science initiatives. Whether you have a question or just
              want to say hi, feel free to reach out!
            </p>
            <div className="social-links">
              <a
                href="https://github.com/rakeshrawat12"
                target="_blank"
                rel="noopener noreferrer"
                className="social-link"
              >
                <span>🐙</span> GitHub
              </a>
              <a
                href="https://linkedin.com"
                target="_blank"
                rel="noopener noreferrer"
                className="social-link"
              >
                <span>💼</span> LinkedIn
              </a>
              <a href="mailto:rakesh.rawat@example.com" className="social-link">
                <span>📧</span> Email
              </a>
            </div>
            <div style={{
              background: 'var(--card-bg)',
              padding: '25px',
              borderRadius: '12px',
              border: '1px solid var(--border)',
              marginTop: '20px'
            }}>
              <p style={{ color: 'var(--secondary)', fontSize: '0.9rem', marginBottom: '10px' }}>
                📍 Location
              </p>
              <p style={{ color: 'var(--light)', fontWeight: '500' }}>India</p>
            </div>
          </div>

          <form className="contact-form" onSubmit={handleSubmit}>
            {status.message && (
              <div className={`form-message ${status.type}`}>
                {status.message}
              </div>
            )}
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
                placeholder="Your Name"
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                placeholder="your.email@example.com"
              />
            </div>
            <div className="form-group">
              <label htmlFor="message">Message</label>
              <textarea
                id="message"
                name="message"
                value={formData.message}
                onChange={handleChange}
                required
                placeholder="Hello, I would like to discuss..."
              />
            </div>
            <button type="submit" className="btn btn-filled" disabled={loading}>
              {loading ? 'Sending...' : 'Send Message'}
            </button>
          </form>
        </div>
      </div>
    </section>
  )
}

export default Contact
