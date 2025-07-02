# genai_draft_email
Agent to provide input prompt for LLM to generate draft email given bullet points

🚀 Features
- Takes plain text bullet points for email draft
- Generates a prompt to be used by AgentOS to make the email draft

Install Steps:

#1 Register Agent .\genai.exe register_agent --name generate_email_prompt --description "This agent returns email prompt"

#2 Create Virtual ENV uv venv uv sync

#3 No Dependencies

#4 Run Agents (AgentOS) .\genai.exe run_agents

#5 Test:
Example Input Text:
Recipient: Sarah, Marketing Director at Bluewave Purpose: Partnership proposal

- Introduce our product
- Highlight mutual benefits
- Suggest a meeting next week

AI Output Draft Email:

Subject: Partnership Proposal for Mutual Growth

Dear Sarah,

I hope this message finds you well. I am reaching out to introduce our product, which I believe aligns well with Bluewave's marketing goals and could bring significant value to both our organizations.

Our product offers innovative features designed to enhance customer engagement and drive sales. By partnering together, we can leverage each other's strengths to create mutually beneficial opportunities, expanding our reach and impact in the market.

I would love to discuss this potential collaboration in more detail and explore how we can work together effectively. Would you be available for a meeting next week at your convenience?

Thank you for considering this proposal. I look forward to your response.

Best regards,
[Your Name]
[Your Position]
[Your Contact Information]
