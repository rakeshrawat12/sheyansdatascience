import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false)
  const [mobileOpen, setMobileOpen] = useState(false)
  const location = window.location.pathname

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <>
      <nav className={`navbar ${scrolled ? 'scrolled' : ''}`}>
        <div className="logo">&lt;RSR /&gt;</div>
        <ul className="nav-links">
          {[
            { path: '/', num: '01', label: 'Home' },
            { path: '/about', num: '02', label: 'About' },
            { path: '/projects', num: '03', label: 'Projects' },
            { path: '/skills', num: '04', label: 'Skills' },
            { path: '/contact', num: '05', label: 'Contact' }
          ].map(({ path, num, label }) => (
            <li key={path}>
              <Link
                to={path}
                className={location === path ? 'active' : ''}
              >
                <span style={{ color: 'var(--primary)', marginRight: '5px' }}>{num}.</span>
                {label}
              </Link>
            </li>
          ))}
        </ul>
        <div
          className={`mobile-menu-btn ${mobileOpen ? 'open' : ''}`}
          onClick={() => setMobileOpen(!mobileOpen)}
        >
          <span></span>
          <span></span>
          <span></span>
        </div>
      </nav>

      <div className={`mobile-nav ${mobileOpen ? 'open' : ''}`}>
        {[
          { path: '/', num: '01', label: 'Home' },
          { path: '/about', num: '02', label: 'About' },
          { path: '/projects', num: '03', label: 'Projects' },
          { path: '/skills', num: '04', label: 'Skills' },
          { path: '/contact', num: '05', label: 'Contact' }
        ].map(({ path, num, label }) => (
          <Link key={path} to={path} onClick={() => setMobileOpen(false)}>
            <span style={{ color: 'var(--primary)' }}>{num}.</span> {label}
          </Link>
        ))}
      </div>
    </>
  )
}

export default Navbar
