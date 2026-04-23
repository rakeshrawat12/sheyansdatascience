import { useEffect, useRef } from 'react'

const projectsData = [
  {
    id: 1,
    title: 'Customer Churn Prediction',
    description:
      'Machine learning model to predict customer churn for a telecom company. Achieved 92% accuracy using Random Forest and XGBoost ensemble methods with comprehensive data preprocessing pipeline.',
    tech: ['Python', 'scikit-learn', 'Pandas', 'XGBoost'],
    github: 'https://github.com',
    icon: '📊'
  },
  {
    id: 2,
    title: 'Sentiment Analysis API',
    description:
      'RESTful API for sentiment analysis of social media posts. Built with Flask and NLP techniques for processing real-time user feedback with high accuracy predictions.',
    tech: ['Python', 'Flask', 'NLTK', 'REST API'],
    github: 'https://github.com',
    icon: '💬'
  },
  {
    id: 3,
    title: 'Sales Analytics Dashboard',
    description:
      'Interactive Tableau dashboard visualizing sales trends, regional performance, and revenue forecasts for a retail chain with real-time data updates.',
    tech: ['Tableau', 'SQL', 'Excel', 'Python'],
    github: 'https://github.com',
    icon: '📈'
  },
  {
    id: 4,
    title: 'Medical Image Classifier',
    description:
      'Deep learning model for classifying medical images using CNN architecture. Integrated with a web application for easy diagnosis support and early disease detection.',
    tech: ['Python', 'TensorFlow', 'Keras', 'Flask'],
    github: 'https://github.com',
    icon: '🖼️'
  },
  {
    id: 5,
    title: 'Stock Price Forecaster',
    description:
      'Stock price prediction system using LSTM networks. Features real-time data processing, customizable alert thresholds, and comprehensive backtesting framework.',
    tech: ['Python', 'TensorFlow', 'Pandas', 'Alpha Vantage'],
    github: 'https://github.com',
    icon: '📉'
  },
  {
    id: 6,
    title: 'Data Quality Analyzer',
    description:
      'Automated tool for detecting data anomalies and quality issues in large datasets. Reduces data cleaning time by 60% with automated reporting and visualizations.',
    tech: ['Python', 'Pandas', 'NumPy', 'SQLAlchemy'],
    github: 'https://github.com',
    icon: '🔍'
  }
]

const Projects = () => {
  const cardRefs = useRef([])

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible')
          }
        })
      },
      { threshold: 0.1 }
    )

    cardRefs.current.forEach((ref) => {
      if (ref) observer.observe(ref)
    })

    return () => observer.disconnect()
  }, [])

  return (
    <section className="section" id="projects">
      <div className="container">
        <h2 className="section-title" data-number="03.">
          Featured Projects
        </h2>
        <div className="projects-grid">
          {projectsData.map((project, index) => (
            <div
              key={project.id}
              className="project-card animate-on-scroll"
              ref={(el) => cardRefs.current[index] = el}
            >
              <div className="project-header">
                <h3>{project.title}</h3>
                <span className="folder-icon">{project.icon}</span>
              </div>
              <p>{project.description}</p>
              <div className="tech-tags">
                {project.tech.map((tech, i) => (
                  <span key={i} className="tech-tag">{tech}</span>
                ))}
              </div>
              <div className="project-links">
                <a href={project.github} target="_blank" rel="noopener noreferrer">
                  View Project <span>↗</span>
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default Projects
