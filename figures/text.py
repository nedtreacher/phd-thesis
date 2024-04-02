from PIL import Image, ImageDraw, ImageFont

def create_text_image(text, font_path, font_size, image_path):
    # Create an image with a white background
    image = Image.new("RGB", (400, 200), "white")

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # x1 - x0
    text_height = text_bbox[3] - text_bbox[1]  # y1 - y0
    text_x = (image.width - text_width) / 2
    text_y = (image.height - text_height) / 2

    # Draw the text on the image
    draw.text((text_x, text_y), text, font=font, fill="black")

    # Calculate padding
    padding_x = 5
    padding_y = 40

    # Define cropping region
    crop_region = (
        int(text_x - padding_x),
        int(text_y - padding_y),
        int(text_x + text_width + padding_x),
        int(text_y + text_height + padding_y)
    )

    # Crop the image
    image = image.crop(crop_region)

    # Save the image
    image.save(image_path)
    print(f"Image saved to {image_path}")

# Example usage
text = "(d)"
font_path = "C:\\Users\\perkinne\\OneDrive - Victoria University of Wellington - STAFF\\Ned_Natalie_PhD\\PhD-thesis\\lm\\lmroman10-regular-webfont.ttf"  # Load font from non-system .ttf file
font_size = 80
image_path = f"figures\\{text}.png"

create_text_image(text, font_path, font_size, image_path)