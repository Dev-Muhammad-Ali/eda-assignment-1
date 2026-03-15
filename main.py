import gradio as gr
import pandas as pd
import os
from datetime import datetime

CONTACT_FILE = "contacts.csv"

if not os.path.exists(CONTACT_FILE):
    pd.DataFrame(columns=["time","name","email","message"]).to_csv(CONTACT_FILE,index=False)


def send_message(name,email,message):

    time = datetime.now()

    new_entry = pd.DataFrame({
        "time":[time],
        "name":[name],
        "email":[email],
        "message":[message]
    })

    df = pd.read_csv(CONTACT_FILE)
    df = pd.concat([df,new_entry],ignore_index=True)
    df.to_csv(CONTACT_FILE,index=False)

    return "Message received successfully. Thank you."


CSS = """

footer {visibility:hidden;}

body{
    background:#0a0a0a;
    color:white;
}

/* Navbar theme */

button{
    background:#111;
    color:#4db8ff;
    border:1px solid #4db8ff;
}

button:hover{
    background:#4db8ff;
    color:black;
}

/* headings */

h1,h2,h3{
    color:#4db8ff;
}

/* skills */

.skill{
    margin-bottom:12px;
}

.progress{
    background:#333;
    border-radius:10px;
    height:10px;
}

.bar{
    background:#4db8ff;
    height:10px;
    border-radius:10px;
}

.profile-image img:hover{
    background: none !important;
}

.profile-image img {
    width: 300px !important;   /* desired width */
    height: auto !important;   /* keeps aspect ratio */
    border-radius: 10px;       /* optional, rounded corners */
}

.gradio-image {
    border: none !important;
    padding: 0 !important;
    background: none !important;
    width: 400px !important;   /* your desired width */
    height: auto !important;   /* maintain aspect ratio */
    pointer-events: none;      /* disables click effect */
}

.gradio-image:hover {
    background: none !important;
}



"""


with gr.Blocks(css=CSS) as demo:

    with gr.Tabs():

        # HOME
        with gr.Tab("Home"):

            with gr.Row():

                
                
                with gr.Column(scale=1):
                    gr.Image(
                        "profile.jpeg",
                        elem_classes="profile-image",
                        show_label=False
                    )

                with gr.Column():

                    gr.Markdown("""
# Muhammad Ali

### Embedded Systems Engineer | AI Developer

Welcome to my professional portfolio.

I specialize in:

• Embedded Systems  
• Artificial Intelligence  
• Hardware Design  
• Python Programming  
• Custom Processor Design  

This portfolio highlights my background, engineering projects, and technical skills.
""")


        # PROFESSIONAL BACKGROUND
        with gr.Tab("Professional Background"):

            gr.Markdown("## Experience")

            gr.Markdown("""
Freelancer – Remote (2023 – Present)

• Developed embedded system solutions  
• Built AI automation tools  
• Designed integrated hardware/software systems
""")

            gr.Markdown("""
Freelancer – Remote (2022 – 2023)

• Created web applications  
• Developed Python automation tools
""")

            gr.Markdown("## Education")

            gr.Markdown("""
BS Embedded Systems  
University of Lahore (Ongoing)

Intermediate – ICS  
Punjab Group of Colleges

Matric – Computer Science
""")


        # PROJECTS
        with gr.Tab("Projects"):

            gr.Markdown("## Engineering Projects")

            with gr.Accordion("AI Jarvis Bot"):

                gr.Markdown("""
An AI-powered voice assistant capable of performing automation tasks using voice commands.

The assistant integrates speech recognition, natural language processing, and automation tools to control applications, retrieve information, and assist with everyday computing tasks.
""")


            with gr.Accordion("16-Bit Custom Processor"):

                gr.Markdown("""
A custom designed 16-bit processor architecture developed using digital logic design.

The processor contains key components such as:

• Arithmetic Logic Unit (ALU)  
• Register File  
• Program Counter  
• Instruction Decoder
""")


            with gr.Accordion("Motor Driver PCB"):

                gr.Markdown("""
A custom designed motor driver printed circuit board used to control DC motors.

Key features include:

• H-bridge motor driver design  
• MOSFET switching for high current  
• Protection circuitry  
• Efficient power handling
""")


        # SKILLS
        with gr.Tab("Skill Sets"):

            gr.Markdown("## Technical Skills")

            gr.HTML("""

<div class="skill">
Python
<div class="progress"><div class="bar" style="width:95%"></div></div>
</div>

<div class="skill">
Verilog
<div class="progress"><div class="bar" style="width:90%"></div></div>
</div>

<div class="skill">
Embedded Systems
<div class="progress"><div class="bar" style="width:85%"></div></div>
</div>

<div class="skill">
PCB Design
<div class="progress"><div class="bar" style="width:80%"></div></div>
</div>

<div class="skill">
AI Development
<div class="progress"><div class="bar" style="width:85%"></div></div>
</div>

""")


        # CONTACT
        with gr.Tab("Contact Me"):

            with gr.Row():

                # LEFT SIDE CONTACT INFO
                with gr.Column():

                    gr.Markdown("""
## Contact Information

📧 **Email:**  
muhammad.ali.abid.dev@gmail.com

📱 **Phone:**  
0333-5949705

📍 **Location:**  
Pakistan

Feel free to reach out for collaborations, freelance work, or engineering projects.
""")


                # RIGHT SIDE CONTACT FORM
                with gr.Column():

                    gr.Markdown("## Send a Message")

                    name = gr.Textbox(label="Name")
                    email = gr.Textbox(label="Email")
                    message = gr.Textbox(label="Message",lines=5)

                    submit = gr.Button("Send Message")

                    output = gr.Textbox(label="Status")

                    submit.click(
                        send_message,
                        inputs=[name,email,message],
                        outputs=output
                    )


demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860)),
    share=False
)
