class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def invert(image):
            return [0 if i == 1 else 1 for i in image]

        def flip(image):
            return image[::-1]
        new_img = [image[i][:] for i in range(len(image))]
        for idx, line in enumerate(new_img):
            new_img[idx] = invert(flip(line))
        return new_img
