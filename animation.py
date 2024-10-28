from manim import *
import numpy as np
from PIL import Image
from manim import FadeOut, FadeIn

class EmoTalkGenStep1to6(MovingCameraScene):
    def construct(self):
        # Set up the camera
        self.camera.frame.save_state()
        
        # Step 1: Speech Input (Waveform)
        t = np.linspace(0, 4*np.pi, 100)
        waveform = FunctionGraph(lambda x: 0.5*np.sin(x) + 0.3*np.sin(2*x) + 0.2*np.sin(3*x), x_range=[0, 4*np.pi], color=BLUE)
        waveform.scale(0.5).move_to(ORIGIN)
        speech_text = Text("Speech Input", font_size=24).next_to(waveform, UP)
        speech_group = VGroup(waveform, speech_text)
        
        self.play(Create(speech_group))
        self.wait(1)
        
        # Step 2: Dynamic Emotion Changer
        emotion_changer = Rectangle(width=3, height=2, fill_color=GREEN, fill_opacity=0.2, stroke_color=GREEN)
        emotion_text = Text("Dynamic Emotion Changer", font_size=24).next_to(emotion_changer, UP)
        emotion_group = VGroup(emotion_changer, emotion_text).next_to(speech_group, RIGHT, buff=2)
        
        arrow1 = Arrow(waveform.get_right(), emotion_changer.get_left(), color=WHITE)
        
        self.play(
            self.camera.frame.animate.move_to(emotion_group).scale(1.2),
            Create(emotion_group),
            Create(arrow1)
        )
        self.wait(1)
        
        # Emotion Analysis Animation
        emotion_labels = VGroup(
            Text("Angry", color=RED, font_size=20),
            Text("Happy", color=YELLOW, font_size=20),
            Text("Sad", color=BLUE, font_size=20),
            Text("Surprised", color=PURPLE, font_size=20)
        ).arrange(DOWN, buff=0.2).move_to(emotion_changer)
        
        self.play(Write(emotion_labels))
        self.wait(1)
        
        # Step 3: Text Encoder
        text_encoder = Rectangle(width=3, height=2, fill_color=ORANGE, fill_opacity=0.2, stroke_color=ORANGE)
        encoder_text = Text("Text Encoder", font_size=24).next_to(text_encoder, UP)
        encoder_group = VGroup(text_encoder, encoder_text).next_to(emotion_group, RIGHT, buff=2)
        
        arrow2 = Arrow(emotion_changer.get_right(), text_encoder.get_left(), color=WHITE)
        
        self.play(
            self.camera.frame.animate.move_to(encoder_group).scale(1.2),
            Create(encoder_group),
            Create(arrow2)
        )
        self.wait(1)
        
        # Latent Representation Animation
        text_latent = self.create_latent_representation(text_encoder, "Text Latent")
        self.play(Create(text_latent))
        self.wait(1)
        
        # Step 4: Image Codec Encoder
        image_encoder = Rectangle(width=3, height=2, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE)
        image_encoder_text = Text("Image Codec Encoder", font_size=24).next_to(image_encoder, UP)
        image_encoder_group = VGroup(image_encoder, image_encoder_text).next_to(speech_group, DOWN, buff=2)
        
        # Load and display the face image
        face_image = self.load_image("/Users/rajathdb/Emo-TalkGen/media/images/face.png", height=1.5)
        face_image.next_to(image_encoder, LEFT)
        
        self.play(
            self.camera.frame.animate.move_to(image_encoder).scale(1.2),
            Create(image_encoder_group),
            FadeIn(face_image)
        )
        self.wait(1)
        
        # Animate feature extraction
        features = VGroup(*[Line(start=face_image.get_corner(corner), end=image_encoder.get_left()) 
                            for corner in [UL, UR, DL, DR, ORIGIN]])
        self.play(Create(features))
        self.wait(1)
        
        # Create latent representation for image
        image_latent = self.create_latent_representation(image_encoder, "Image Latent")
        self.play(Create(image_latent))
        self.wait(1)
        
        # Step 5: Diffusion Model
        diffusion_model = Rectangle(width=4, height=3, fill_color=GREEN, fill_opacity=0.2, stroke_color=GREEN)
        diffusion_text = Text("Diffusion Model", font_size=24).next_to(diffusion_model, UP)
        diffusion_group = VGroup(diffusion_model, diffusion_text).next_to(encoder_group, RIGHT, buff=3)
        
        self.play(
            self.camera.frame.animate.move_to(diffusion_group).scale(1.5),
            Create(diffusion_group)
        )
        
        # Animate combining latents
        text_latent_copy = text_latent.copy()
        image_latent_copy = image_latent.copy()
        self.play(
            text_latent_copy.animate.move_to(diffusion_model.get_left()),
            image_latent_copy.animate.move_to(diffusion_model.get_bottom())
        )
        self.wait(1)
        
        # Animate diffusion process
        noise = VGroup(*[Dot(radius=0.05, color=WHITE).move_to(
            diffusion_model.get_center() + np.array([np.random.uniform(-1, 1), np.random.uniform(-1, 1), 0])
        ) for _ in range(50)])
        
        self.play(Create(noise))
        self.play(noise.animate.arrange_in_grid(rows=5, cols=10, buff=0.2).move_to(diffusion_model))
        self.wait(1)
        
        # Step 6: Conditional Function (C) and CFG
        conditional_func = Rectangle(width=3, height=2, fill_color=PURPLE, fill_opacity=0.2, stroke_color=PURPLE)
        conditional_text = Text("Conditional Function (C)", font_size=20).next_to(conditional_func, UP)
        conditional_group = VGroup(conditional_func, conditional_text).next_to(diffusion_group, UP, buff=1.5)

        self.play(
            self.camera.frame.animate.move_to(conditional_group).scale(1.5),
            Create(conditional_group)
        )

        # Conditional inputs
        inputs = VGroup(
            Text("Facial Expressions", font_size=16),
            Text("Lip Movements", font_size=16),
            Text("Other Parameters", font_size=16)
        ).arrange(DOWN, buff=0.2).next_to(conditional_func, LEFT)

        self.play(Write(inputs))

        # Arrow to Diffusion Model
        arrow_to_diffusion = Arrow(conditional_func.get_bottom(), diffusion_group.get_top(), color=WHITE)
        self.play(Create(arrow_to_diffusion))

        # CFG
        cfg_box = Rectangle(width=3, height=2, fill_color=YELLOW, fill_opacity=0.2, stroke_color=YELLOW)
        cfg_text = Text("Classifier-Free Guidance", font_size=20).next_to(cfg_box, UP)
        cfg_group = VGroup(cfg_box, cfg_text).next_to(conditional_group, RIGHT, buff=2)

        self.play(
            self.camera.frame.animate.move_to(VGroup(conditional_group, cfg_group).get_center()).scale(1.2),
            Create(cfg_group)
        )

        # CFG explanation
        cfg_explanation = Text("Enables more natural\nand varied expressions", font_size=16).move_to(cfg_box)
        self.play(Write(cfg_explanation))

        # Arrow from CFG to Diffusion Model
        arrow_cfg_to_diffusion = Arrow(cfg_box.get_bottom(), diffusion_group.get_top(), color=WHITE)
        self.play(Create(arrow_cfg_to_diffusion))

        # Zoom in on both conditional function and CFG groups
        self.play(
            self.camera.frame.animate.move_to(VGroup(conditional_group, cfg_group).get_center()).scale(1.5),
        )
        self.wait(2)

        # Step 7: 3DMM Coefficients Extraction
        coeff_extractor = Rectangle(width=3, height=2, fill_color=RED, fill_opacity=0.2, stroke_color=RED)
        coeff_text = Text("3DMM Coefficients\nExtraction", font_size=20).next_to(coeff_extractor, UP)
        coeff_group = VGroup(coeff_extractor, coeff_text).next_to(image_encoder_group, RIGHT, buff=2)

        self.play(
            self.camera.frame.animate.move_to(coeff_group).scale(1.5),
            Create(coeff_group)
        )

        # Facial Dynamics Animation
        dynamics_text = Text("Facial Dynamics", font_size=16).next_to(coeff_extractor, LEFT)
        arrow_to_extractor = Arrow(face_image.get_right(), coeff_extractor.get_left(), color=WHITE)

        self.play(
            Write(dynamics_text),
            Create(arrow_to_extractor)
        )

        # Coefficients Animation
        coeffs = VGroup(*[
            Text(f"Coeff {i}", font_size=14) for i in range(1, 6)
        ]).arrange(DOWN, buff=0.1).move_to(coeff_extractor)

        self.play(Write(coeffs))

        # Arrow to Diffusion Model
        arrow_to_diffusion = Arrow(coeff_extractor.get_right(), diffusion_model.get_left(), color=WHITE)
        guidance_text = Text("Expression Guidance", font_size=16).next_to(arrow_to_diffusion, UP)

        self.play(
            Create(arrow_to_diffusion),
            Write(guidance_text)
        )

        # Keep focus on the 3DMM Coefficients Extraction
        self.wait(2)

        # Final output
        output_face = face_image.copy().scale(1.5).next_to(diffusion_group, RIGHT, buff=1)
        output_text = Text("Final Output", font_size=20).next_to(output_face, DOWN)
        self.play(
            self.camera.frame.animate.move_to(diffusion_group),
            FadeOut(noise),
            FadeIn(output_face),
            Write(output_text)
        )

        # Show the entire system
        self.play(
            self.camera.frame.animate.move_to(diffusion_group),
        )
        self.wait(2)

    def create_latent_representation(self, reference_obj, label_text):
        latent_rep = Rectangle(width=2.5, height=1.5, fill_color=YELLOW, fill_opacity=0.2, stroke_color=YELLOW).next_to(reference_obj, RIGHT)
        latent_text = Text(label_text, font_size=20).next_to(latent_rep, UP, buff=0.1)
        
        vector_values = [0.8, -0.3, 0.5, 0.2, -0.7]
        vector_rects = VGroup(*[Rectangle(width=0.3, height=abs(val)*0.5, fill_opacity=1, fill_color=BLUE if val > 0 else RED) for val in vector_values])
        vector_rects.arrange(RIGHT, buff=0.1).move_to(latent_rep)
        
        vector_labels = VGroup(*[Text(f"{val:.1f}", font_size=16).next_to(rect, DOWN if val > 0 else UP) for val, rect in zip(vector_values, vector_rects)])
        
        return VGroup(latent_rep, latent_text, vector_rects, vector_labels)

    def load_image(self, path, height=1):
        img = Image.open(path)
        img_array = np.array(img)
        manim_image = ImageMobject(img_array).set_height(height)
        return manim_image

# Run the animation
if __name__ == "__main__":
    scene = EmoTalkGenStep1to6()
    scene.render()

