import os
import tkinter as tk
from PIL import Image, ImageTk


class ImageBrowser:
    def __init__(self, master, folder_path):
        self.master = master
        self.folder_path = folder_path
        self.images = []
        self.current_index = 0
        self.delay = 50  # time between images in milliseconds

        # create canvas
        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # bind left and right arrow keys
        self.master.bind("<Left>", self.previous_image)
        self.master.bind("<Right>", self.next_image)

        # load images
        self.load_images()

    def load_images(self):
        file_names = os.listdir(self.folder_path)
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif')

        # filter out non-image files
        image_names = [fn for fn in file_names if fn.endswith(image_extensions)]

        # sort the image names by their numeric value
        image_names = sorted(image_names, key=lambda x: int(''.join(filter(str.isdigit, x))) if ''.join(filter(str.isdigit, x)) else -1)

        self.images = []
        for name in image_names:
            img = Image.open(os.path.join(self.folder_path, name))
            self.images.append(img)

        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        # clear canvas
        self.canvas.delete("all")

        # load image and resize canvas
        image = self.images[self.current_index]
        self.image_tk = ImageTk.PhotoImage(image)
        self.canvas.config(width=image.width, height=image.height)

        # add image to canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)

    def next_image(self, event):
        # increment current index and load image
        self.current_index = (self.current_index + 1) % len(self.images)
        self.load_image()

    def previous_image(self, event):
        # decrement current index and load image
        self.current_index = (self.current_index - 1) % len(self.images)
        self.load_image()

    def start_slideshow(self):
        # start the slideshow by scheduling the update_image function to run after a delay
        self.update_image()

    def stop_slideshow(self):
        # stop the slideshow by canceling the scheduled function call
        self.canvas.after_cancel(self.update_id)

    def update_image(self):
        # increment current index and load image
        self.current_index = (self.current_index + 1) % len(self.images)
        self.load_image()

        # schedule the next update after a delay
        self.update_id = self.canvas.after(self.delay, self.update_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageBrowser(root, "./images")
    app.start_slideshow()
    root.mainloop()
