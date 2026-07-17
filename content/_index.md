---
title: ''
summary: 'AI for Earth observation, remote sensing, and climate applications.'
date: 2026-07-17
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      text: ''
      headings:
        about: ''
        education: Education
        interests: Research interests
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  - block: markdown
    id: research
    content:
      title: My Research
      subtitle: Reliable AI for understanding a changing Earth
      text: |-
        I study how machine learning can extract reliable information from satellite imagery. My work combines remote sensing, computer vision, and synthetic data to improve change detection and environmental monitoring.

        Current directions include multimodal Earth observation, data-efficient learning, and methods that remain useful across sensors, regions, and changing environmental conditions.
    design:
      columns: '1'

  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: recent-publications
    content:
      title: Recent Publications
      filters:
        folders:
          - publications
        exclude_featured: true
    design:
      view: citation
---
