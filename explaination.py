from manim import *
import numpy as np

class EmoTalkGenAnimation(MovingCameraScene):
    def construct(self):
        # Create a cute waveform
        t = np.linspace(0, 4*np.pi, 1000)
        waveform = ParametricFunction(
            lambda t: np.array([t/4, 0.3*np.sin(t) + 0.1*np.sin(3*t), 0]),
            t_range=[0, 4*np.pi],
            color=BLUE
        )
        
        # Scale and position the waveform
        waveform.scale(0.5).move_to(3*LEFT)
        
        # Add a label for the waveform
        waveform_label = Text("Speech Input", font_size=24).next_to(waveform, UP, buff=0.2)
        
        # Group the waveform and its label
        waveform_group = VGroup(waveform, waveform_label)
        
        # Animate the creation of waveform
        self.play(Create(waveform_group))
        self.wait(0.5)

        # Create an arrow starting from the waveform
        arrow = Arrow(waveform.get_right(), waveform.get_right() + RIGHT * 5, buff=0.3)
        
        # Animate the creation of the arrow
        self.play(Create(arrow))
        self.wait(0.5)

        # Move camera to focus on the arrow's end
        self.play(
            self.camera.frame.animate.move_to(arrow.get_end()).scale(0.75),
            run_time=1.5
        )

        # Create the Dynamic Emotion Changer node
        emotion_changer = Rectangle(width=3, height=2, fill_color=GREEN, fill_opacity=0.2)
        emotion_changer.move_to(arrow.get_end() + RIGHT * 1.5)
        emotion_label = Text("Dynamic Emotion\nChanger", font_size=24).move_to(emotion_changer)
        
        # Animate the creation of the emotion changer node
        self.play(Create(emotion_changer), Write(emotion_label))
        self.wait(0.5)

        # Add explanation text for Dynamic Emotion Changer
        explanation = Text("Analyzes speech and\nidentifies emotional tone", font_size=18, color=YELLOW)
        explanation.next_to(emotion_changer, UP, buff=0.3)
        self.play(Write(explanation))
        self.wait(1)

        # Extend the arrow to connect to the emotion changer
        new_arrow = Arrow(waveform.get_right(), emotion_changer.get_left(), buff=0.3)
        self.play(Transform(arrow, new_arrow))
        self.wait(0.5)

        # Animate a pulse along the arrow
        dot = Dot(color=YELLOW).move_to(arrow.get_start())
        self.play(dot.animate.move_to(arrow.get_end()), run_time=1)
        self.remove(dot)
        
        # Create output arrow and text
        output_arrow = Arrow(emotion_changer.get_right(), emotion_changer.get_right() + RIGHT * 2, buff=0.3)
        output_text = Text("Emotional labels", font_size=18, color=YELLOW)
        output_text.next_to(output_arrow, UP, buff=0.2)
        
        self.play(Create(output_arrow), Write(output_text))
        self.wait(1)
        
        # Move camera back to show the entire scene
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).scale(1/0.75),
            run_time=1.5
        )
        
        # Create the emotion text
        emotions = ["Happy", "Sad", "Angry", "Surprised"]
        emotion_text = Text(emotions[0], font_size=20, color=RED).next_to(emotion_changer, DOWN)
        
        # Show the emotion text
        self.play(Write(emotion_text))
        self.wait(0.5)
        
        # Cycle through emotions
        for emotion in emotions[1:] + emotions[:1]:
            self.play(emotion_text.animate.become(
                Text(emotion, font_size=20, color=RED).next_to(emotion_changer, DOWN)
            ))
            self.wait(0.5)
        
        self.wait(1)

        # Create the Text Encoder node
        text_encoder = Rectangle(width=3, height=2, fill_color=BLUE, fill_opacity=0.2)
        text_encoder.next_to(emotion_changer, RIGHT, buff=2)
        encoder_label = Text("Text Encoder", font_size=24).move_to(text_encoder)
        
        # Create latent representation
        text_latent_rep = self.create_latent_representation(text_encoder, "Text Latent")
        text_latent_rep.next_to(text_encoder, RIGHT, buff=0.5)
        
        # Group Text Encoder and latent representation
        encoder_group = VGroup(text_encoder, encoder_label, text_latent_rep)
        
        # Move camera to focus on the area including Emotion Changer, Text Encoder, and latent representation
        self.play(
            self.camera.frame.animate.move_to(encoder_group.get_center()).scale(0.6),
            run_time=1.5
        )

        # Animate the creation of the Text Encoder node
        self.play(Create(text_encoder), Write(encoder_label))
        self.wait(0.5)

        # Create and animate the arrow from Emotion Changer to Text Encoder
        arrow_to_encoder = Arrow(emotion_changer.get_right(), text_encoder.get_left(), buff=0.3)
        self.play(Create(arrow_to_encoder))
        self.wait(0.5)

        # Animate a pulse along the arrow
        dot = Dot(color=YELLOW).move_to(arrow_to_encoder.get_start())
        self.play(dot.animate.move_to(arrow_to_encoder.get_end()), run_time=1)
        self.remove(dot)

        # Add explanation text for Text Encoder
        encoder_explanation = Text("Converts emotional labels\ninto latent representation", font_size=18, color=YELLOW)
        encoder_explanation.next_to(text_encoder, UP, buff=0.3)
        self.play(Write(encoder_explanation))
        self.wait(1)

        # Animate the creation of latent representation
        self.play(Create(text_latent_rep))
        self.wait(1)

        # Move camera back to show the entire scene
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).scale(1/0.6),
            run_time=1.5
        )

        self.wait(2)

        # Step 4: Image Codec Encoder (Ie)
        
         # Create image input
        face_image = ImageMobject("/Users/rajathdb/Emo-TalkGen/media/images/face.png").scale(0.99)  # Replace with actual image path
        face_image.to_edge(LEFT, buff=1)
        face_image.shift(DOWN * 3)  # Move it down to avoid overlap
        image_label = Text("Speaker's Face", font_size=20).next_to(face_image, DOWN)
        image_input_group = Group(face_image, image_label)
        
        # Move camera to focus on the image input
        self.play(
            self.camera.frame.animate.move_to(image_input_group).scale(0.99),
            run_time=1.5
        )

        # Animate the creation of the image input
        self.play(FadeIn(image_input_group))
        self.wait(0.5)

        # Create the Image Codec Encoder node
        image_encoder = Rectangle(width=3, height=2, fill_color=PURPLE, fill_opacity=0.2)
        image_encoder.next_to(face_image, RIGHT, buff=2)
        image_encoder_label = Text("Image Codec\nEncoder (Ie)", font_size=24).move_to(image_encoder)
        
        # Move camera to include both image input and encoder
        self.play(
            self.camera.frame.animate.move_to((face_image.get_center() + image_encoder.get_center()) / 2),
            run_time=1.5
        )

        # Animate the creation of the Image Encoder node
        self.play(Create(image_encoder), Write(image_encoder_label))
        self.wait(0.5)

        # Create and animate the arrow from image to Image Encoder
        arrow_to_image_encoder = Arrow(face_image.get_right(), image_encoder.get_left(), buff=0.3)
        self.play(Create(arrow_to_image_encoder))
        self.wait(0.5)

        # Animate a pulse along the arrow
        dot = Dot(color=YELLOW).move_to(arrow_to_image_encoder.get_start())
        self.play(dot.animate.move_to(arrow_to_image_encoder.get_end()), run_time=1)
        self.remove(dot)

        # Add explanation text for Image Encoder
        image_encoder_explanation = Text("Extracts facial features\nand dynamics", font_size=18, color=YELLOW)
        image_encoder_explanation.next_to(image_encoder, UP, buff=0.3)
        self.play(Write(image_encoder_explanation))
        self.wait(1)

        # Create latent representation for Image Encoder
        image_latent_rep = self.create_latent_representation(image_encoder, "Image Latent")
        image_latent_rep.next_to(image_encoder, RIGHT, buff=0.5)
        
        # Move camera to include encoder and latent representation
        self.play(
            self.camera.frame.animate.move_to((image_encoder.get_center() + image_latent_rep.get_center()) / 2),
            run_time=1.5
        )

        # Animate the creation of image latent representation
        self.play(Create(image_latent_rep))
        self.wait(1)

        # Move camera back to show the entire scene
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).scale(1/0.6),
            run_time=1.5
        )

        self.wait(2)

        # Step 5: Diffusion Model and related components

        # # Create Facial Dynamic Latent representation
        # facial_dynamic_latent = self.create_latent_representation(image_encoder, "Facial Dynamic\nLatent")
        # facial_dynamic_latent.next_to(image_latent_rep, RIGHT, buff=1)

        # # Move camera to focus on Facial Dynamic Latent
        # self.play(
        #     self.camera.frame.animate.move_to(facial_dynamic_latent.get_center()).scale(0.75),
        #     run_time=1.5
        # )

        # # Animate the creation of Facial Dynamic Latent
        # self.play(Create(facial_dynamic_latent))
        # self.wait(0.5)

        # # Create arrow from Image Latent to Facial Dynamic Latent
        # arrow_to_facial_dynamic = Arrow(image_latent_rep.get_right(), facial_dynamic_latent.get_left(), buff=0.3)
        # self.play(Create(arrow_to_facial_dynamic))
        # self.wait(0.5)

        # Create Diffusion Model node
        diffusion_model = Rectangle(width=4, height=2.5, fill_color=RED, fill_opacity=0.2)
        diffusion_model.next_to(image_latent_rep, DOWN, buff=2)
        diffusion_label = Text("Diffusion Model", font_size=24).move_to(diffusion_model)

        # Create Conditional Function node
        conditional_function = Rectangle(width=3, height=2, fill_color=ORANGE, fill_opacity=0.2)
        conditional_function.next_to(image_latent_rep, RIGHT, buff=1.5)
        conditional_label = Text("Conditional\nFunction (C)", font_size=20).move_to(conditional_function)

        # Move camera to include Diffusion Model and Conditional Function
        self.play(
            self.camera.frame.animate.move_to((diffusion_model.get_center() + conditional_function.get_center()) / 2),
            run_time=1.5
        )

        # Animate the creation of Diffusion Model and Conditional Function
        self.play(Create(diffusion_model), Write(diffusion_label))
        self.play(Create(conditional_function), Write(conditional_label))
        self.wait(0.5)

        # Create arrows to Diffusion Model
        self.play(
            self.camera.frame.animate.move_to(text_latent_rep).scale(1.05),
        )
        arrow_text_to_conditional = Arrow(text_latent_rep.get_bottom(), conditional_function.get_right(), buff=0.3, path_arc=-1)
        arrow_facial_to_conditional = Arrow(image_latent_rep.get_right(), conditional_function.get_left(), buff=0.3)
        arrow_conditional_to_diffusion = Arrow(conditional_function.get_bottom(), diffusion_model.get_right(), buff=0.3, path_arc=-1)

        # Animate the creation of arrows
        self.play(Create(arrow_text_to_conditional), Create(arrow_facial_to_conditional), Create(arrow_conditional_to_diffusion))
        self.wait(0.5)
        self.play(
            self.camera.frame.animate.move_to(diffusion_model).scale(1.05),
        )

        # Add explanation text for Diffusion Model
        diffusion_explanation = Text("Blends latent representations\nto produce coherent and\nemotionally consistent\nvisual representation", font_size=16, color=YELLOW)
        diffusion_explanation.next_to(diffusion_model, DOWN, buff=0.3)
        self.play(Write(diffusion_explanation))
        self.wait(1)


        # Create Face latent representation Model node
        face_latent_representation = Rectangle(width=4, height=2.5, fill_color=RED, fill_opacity=0.2)
        face_latent_representation.next_to(diffusion_model, DOWN, buff=2)
        face_latent_representation_label = Text("Face Dynamics\nLatent\nRepresentation", font_size=24).move_to(face_latent_representation)

        # Animate the creation of Diffusion Model and Conditional Function
        self.play(Create(face_latent_representation), Write(face_latent_representation_label))
        self.wait(0.5)

        # Create output from Diffusion Model
        diffusion_output_arrow = Arrow(diffusion_model.get_left(), face_latent_representation.get_left(), buff=0.3, path_arc=1)
        diffusion_output_text = Text("Generated\nFacial Expressions", font_size=18, color=GREEN)
        diffusion_output_text.next_to(diffusion_output_arrow, LEFT*0.5, buff=0.2)

        self.play(Create(diffusion_output_arrow), Write(diffusion_output_text))
        self.wait(1)

       
        

        self.wait(2)

        # Step 6: Codec Decoder

        # Create Codec Decoder node
        codec_decoder = self.create_codec_decoder()
        codec_decoder.next_to(face_latent_representation, RIGHT, buff=2)

        # Move camera to include Diffusion Model and Codec Decoder
        self.play(
            self.camera.frame.animate.move_to((face_latent_representation.get_center() + codec_decoder.get_center()) / 2).scale(0.85),
            run_time=1.5
        )

        # Animate the creation of Codec Decoder node
        self.play(Create(codec_decoder))
        self.wait(0.5)

        # Create and animate the arrow from Diffusion Model to Codec Decoder
        arrow_to_codec_decoder = Arrow(face_latent_representation.get_right(), codec_decoder.get_left(), buff=0.3)
        self.play(Create(arrow_to_codec_decoder))
        self.wait(0.5)

        # Add explanation text for Codec Decoder
        codec_decoder_explanation = Text("Decodes latent representations\ninto 3DMM output coefficients", font_size=18, color=YELLOW)
        codec_decoder_explanation.next_to(codec_decoder, UP, buff=0.3)
        
        self.play(Write(codec_decoder_explanation))
        self.wait(1)

        # Move camera back to show the entire scene
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).scale(0.99),
            run_time=1.5
        )

        self.wait(2)

    # ... (keep the create_latent_representation method)
    def create_latent_representation(self, reference_obj, label_text):
        latent_rep = Rectangle(width=2.5, height=1.5, fill_color=YELLOW, fill_opacity=0.2, stroke_color=YELLOW)
        latent_text = Text(label_text, font_size=20).next_to(latent_rep, UP, buff=0.1)
        
        vector_values = [0.8, -0.3, 0.5, 0.2, -0.7]
        vector_rects = VGroup(*[Rectangle(width=0.3, height=abs(val)*0.5, fill_opacity=1, fill_color=BLUE if val > 0 else RED) for val in vector_values])
        vector_rects.arrange(RIGHT, buff=0.1).move_to(latent_rep)
        
        vector_labels = VGroup(*[Text(f"{val:.1f}", font_size=16).next_to(rect, DOWN if val > 0 else UP) for val, rect in zip(vector_values, vector_rects)])
        
        return VGroup(latent_rep, latent_text, vector_rects, vector_labels)
    
    def create_codec_decoder(self):
        # Create the main rectangle for the Codec Decoder
        codec_decoder = Rectangle(width=3, height=6, fill_color=PURPLE, fill_opacity=0.2)
        codec_decoder_label = Text("Codec Decoder", font_size=24).move_to(codec_decoder.get_top() + DOWN * 0.5)

        # Create internal elements
        elements = [
            "FiLM", "MLP", "FiLM", "Cross Attn", "FiLM", "Self Attn"
        ]
        element_rects = VGroup(*[
            Rectangle(width=2.5, height=0.5, fill_color=WHITE, fill_opacity=0.2).set_stroke(BLACK, 1)
            for _ in elements
        ])
        element_texts = VGroup(*[
            Text(element, font_size=16)
            for element in elements
        ])
        element_group = VGroup(*[
            VGroup(rect, text).arrange(ORIGIN, buff=0)
            for rect, text in zip(element_rects, element_texts)
        ]).arrange(DOWN, buff=0.2).move_to(codec_decoder)

        # Group all elements together
        return VGroup(codec_decoder, codec_decoder_label, element_group)


# defense day
if __name__ == "__main__":
    scene = EmoTalkGenAnimation()
    scene.render()