import io
import torch
import torchvision

from PIL import Image
from PIL import ImageDraw

torch.manual_seed(1234)

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

# TODO: determine where and when to load model into memory with
# setting the correct configuration
# Load pre-trained model into memory
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()
model.to(device)


def extract_image(image_bytes):
    return Image.open(io.BytesIO(image_bytes))


def object_detection(content):
    orig_img = extract_image(content)
    img_tensor = transform_image(orig_img)
    detections = prediction(img_tensor)
    _ = add_bounding_boxes(orig_img, detections)
    return orig_img


def prediction(tensor):
    out = model([tensor])
    return out[0]


def transform_image(image):
    transform = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor()
    ])
    # TODO: place a check here all images are float32
    return transform(image)


def add_bounding_boxes(image, detections):
    draw = ImageDraw.Draw(image)
    draw.rectangle(detections['boxes'][0].detach().numpy(), outline='red', width=3)
    return draw