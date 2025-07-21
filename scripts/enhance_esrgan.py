from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

model = RealESRGANer(
    scale=4,
    model_path='models/RealESRGAN_x4plus.pth',
    model=RRDBNet(num_in_ch=3, num_out_ch=3, nf=64, nb=23, gc=32)
)

def enhance_plate(plate_img):
    return model.enhance(plate_img, outscale=4)[0]
