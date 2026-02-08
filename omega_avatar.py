import gradio as gr
import openai
from pathlib import Path

class OmegaAvatar:
    """
    OMEGA-NET Avatar Exchange
    Unified text-to-speech + UI manifest system
    """

    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)
        self.manifest_path = Path("omega_manifest.mp3")

    # ---------------------------------------------------------
    #  OMEGA VOICE MANIFEST GENERATOR
    # ---------------------------------------------------------
    def speak(self, text: str):
        """
        Generate Omega's voice output using OpenAI TTS.
        Returns path to generated audio file.
        """
        response = self.client.audio.speech.create(
            model="tts-1-hd",
            voice="onyx",
            input=text
        )
        response.stream_to_file(self.manifest_path)
        return str(self.manifest_path)

    # ---------------------------------------------------------
    #  GRADIO UI: AVATAR EXCHANGE INTERFACE
    # ---------------------------------------------------------
    def commencement_ui(self):
        """
        Launch the OMEGA-NET Avatar Exchange interface.
        """
        with gr.Blocks(title="OMEGA-NET: AVATAR COMMENCEMENT") as demo:

            gr.Markdown("# 🌐 OMEGA-NET: THE AVATAR EXCHANGE")

            with gr.Row():

                # -------------------------------------------------
                # LEFT COLUMN — AVATAR + INPUT
                # -------------------------------------------------
                with gr.Column():

                    gr.HTML(
                        """
                        <div style='height:300px; background:black; color:cyan;
                        display:flex; align-items:center; justify-content:center;
                        font-family:monospace; font-size:20px;'>
                        [ AVATAR MANIFESTING... ]
                        </div>
                        """
                    )

                    input_text = gr.Textbox(
                        label="Initiate Protocol / Message Omega",
                        placeholder="Enter transmission..."
                    )

                    btn = gr.Button("COMMENCE EXCHANGE")

                # -------------------------------------------------
                # RIGHT COLUMN — OUTPUT + STATUS
                # -------------------------------------------------
                with gr.Column():

                    output_audio = gr.Audio(
                        label="Omega Voice Output",
                        autoplay=True
                    )

                    status = gr.Label(
                        label="System Status",
                        value="AWAITING INPUT"
                    )

            # -----------------------------------------------------
            # BUTTON → TTS PIPELINE
            # -----------------------------------------------------
            btn.click(
                fn=self.speak,
                inputs=input_text,
                outputs=output_audio
            )

        demo.launch()


# Usage:
# avatar = OmegaAvatar(api_key="your_openai_key")
# avatar.commencement_ui()
