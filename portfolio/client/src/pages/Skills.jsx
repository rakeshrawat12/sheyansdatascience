import { useEffect, useRef, useState } from 'react'

const skillsData = {
  languages: { name: 'Languages', icon: '💻', skills: [
    { name: 'Python', percentage: 95 },
    { name: 'R', percentage: 80 },
    { name: 'SQL', percentage: 90 },
    { name: 'JavaScript', percentage: 70 }
  ]},
  mlAI: { name: 'Machine Learning & AI', icon: '🤖', skills: [
    { name: 'TensorFlow', percentage: 85 },
    { name: 'PyTorch', percentage: 75 },
    { name: 'scikit-learn', percentage: 90 },
    { name: 'Keras', percentage: 80 }
  ]},
  tools: { name: 'Tools & Platforms', icon: '🛠️', skills: [
    { name: 'Git', percentage: 90 },
    { name: 'Docker', percentage: 70 },
    { name: 'AWS', percentage: 75 },
    { name: 'Tableau', percentage: 85 }
  ]},
  databases: { name: 'Databases', icon: '🗄️', skills: [
    { name: 'MongoDB', percentage: 85 },
    { name: 'PostgreSQL', percentage: 80 },
    { name: 'MySQL', percentage: 75 },
    { name: 'Redis', percentage: 65 }
  ]}
}

const Skills = () => {
  const [visibleSkills, setVisibleSkills] = useState({})
  const skillRefs = useRef([])

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const index = parseInt(entry.target.dataset.index)
            setTimeout(() => {
              setVisibleSkills(prev => ({ ...prev, [index]: true }))
            }, index * 100)
          }
        })
      },
      { threshold: 0.3 }
    )

    skillRefs.current.forEach((ref) => {
      if (ref) observer.observe(ref)
    })

    return () => observer.disconnect()
  }, [])

  let skillIndex = 0

  return (
    <section className="section" id="skills">
      <div className="container">
        <h2 className="section-title" data-number="04.">
          Skills & Technologies
        </h2>
        <div className="skills-grid">
          {Object.values(skillsData).map((category) => (
            <div key={category.name} className="skill-category">
              <h3>
                <span>{category.icon}</span> {category.name}
              </h3>
              {category.skills.map((skill) => {
                const currentIndex = skillIndex++
                return (
                  <div
                    key={skill.name}
                    className="skill-item animate-on-scroll"
                    ref={(el) => skillRefs.current[currentIndex] = el}
                    data-index={currentIndex}
                  >
                    <div className="skill-info">
                      <span className="skill-name">{skill.name}</span>
                      <span className="skill-percentage">{skill.percentage}%</span>
                    </div>
                    <div className="skill-bar">
                      <div
                        className="skill-progress"
                        style={{
                          width: visibleSkills[currentIndex] ? `${skill.percentage}%` : '0%'
                        }}
                      />
                    </div>
                  </div>
                )
              })}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default Skills
