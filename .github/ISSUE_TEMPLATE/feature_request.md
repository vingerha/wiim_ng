name: Feature Request
description: File a idea on how to increase the value.
title: "[FEATURE]: "
labels: ["feature", "triage"]
assignees: 
  - []
body:
  - type: markdown
    attributes:
      value: |
        Is your request really a feature or aiming to fix a bug, then raise a Issue instead
  - type: textarea
    id: description
    attributes:
      label: Describe the solution you'd like
      description: A clear and concise description of what you want to happen.
      render: shell
  - type: textarea
    id: considerations
    attributes:
      label: Describe alternatives you've considered
      description: A clear and concise description of any alternative solutions or features you've considered.
      render: shell
  - type: textarea
    id: additional
    attributes:
      label: Additional context
      description: Add any other context or screenshots about the feature request here.
      render: shell
