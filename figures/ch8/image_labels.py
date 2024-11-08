from PIL import Image, ImageDraw, ImageFont
import os

font_path = "C:\\Users\\perkinne\\OneDrive - Victoria University of Wellington - STAFF\\Ned_Natalie_PhD\\PhD-thesis\\lm\\lmroman10-regular-webfont.ttf"

def add_sidebar(image_path, label, ratio_size):
    # Open the image
    img = Image.open(image_path)
    
    # Resize image to 300 DPI based on height
    width, height = img.size
    new_height = int((height / img.info['dpi'][1]) * 300)
    img = img.resize((int(width * (new_height / height)), new_height))
    
    # Get resized image dimensions
    width, height = img.size
    
    # Define sidebar width and font size relative to the image height and width
    #sidebar_width = (height * width // 20000) // ratio_size
    #font_size = (height * width // 37500) // ratio_size
    
    sidebar_width = (height * width // 37500) // ratio_size
    font_size = (height * width // 55000) // ratio_size
    
    # Create a new image with sidebar
    new_img = Image.new('RGB', (int(width) + int(sidebar_width), int(height)), color='white')
    new_img.paste(img, (int(sidebar_width), 0))
    
    # Draw label
    draw = ImageDraw.Draw(new_img)
    font = ImageFont.truetype(font_path, font_size)  # Load font from non-system .ttf file
    label_position = (sidebar_width // 10, height // 20)  # 5% of sidebar width and 2.5% of image height
    draw.text(label_position, label, fill='black', font=font)
    
    return new_img, width, sidebar_width

def edit_images(image_labels):
    edited_images = []
    total_main_width = 0
    total_sidebar_width = 0
    
    # Edit each image and store the edited images
    for image_filename, label, ratio_size in image_labels:
        image_path = image_filename
        edited_img, width, sidebar_width = add_sidebar(image_path, label, ratio_size)  # Pass ratio_size
        edited_images.append(edited_img)
        total_main_width += width
        total_sidebar_width += sidebar_width
        output_filename = f"{os.path.splitext(image_filename)[0]}_edited.png"
        edited_img.save(output_filename)
    
    # Compute the ratio between the total width of all edited images
    total_width = total_main_width + total_sidebar_width
    ratio = [width / total_width for edited_img, width, _ in zip(edited_images, [img.size[0] for img in edited_images], [img.size[1] // 7.5 for img in edited_images])]
    
    # Output the ratios
    print("Ratio between the widths of the edited images:", ratio)

if __name__ == "__main__":
    # List of tuples containing image filenames, custom labels, and ratio sizes
    image_labels = [
        ("200sccmMFC_carrierline_thruchamber.png", "(a)", 0.5),
        ("500sccmMFC_dilutionline_thruchamber.png", "(b)", 0.5)  # Example of different ratio size
    ]
    
    # Edit specified images
    edit_images(image_labels)

    print("Labels added")