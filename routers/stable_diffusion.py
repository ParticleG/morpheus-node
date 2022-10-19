from importlib import import_module
from fastapi import APIRouter
from pydantic import BaseModel

from internal.utils import images2base64

router = APIRouter()


class PayloadTxt2Img(BaseModel):
    prompt: str
    negative_prompt: str
    prompt_style: str
    prompt_style2: str
    steps: int
    sampler_index: int
    restore_faces: bool
    tiling: bool
    n_iter: int
    batch_size: int
    cfg_scale: float
    seed: int
    subseed: int
    subseed_strength: float
    seed_resize_from_h: int
    seed_resize_from_w: int
    seed_enable_extras: bool
    height: int
    width: int
    enable_hr: bool
    denoising_strength: float
    firstphase_width: int
    firstphase_height: int


class PayloadImg2Img(BaseModel):
    mode: int
    prompt: str
    negative_prompt: str
    prompt_style: str
    prompt_style2: str
    init_img: str
    init_img_with_mask: str
    init_img_inpaint: str
    init_mask_inpaint: str
    mask_mode: int
    steps: int
    sampler_index: int
    mask_blur: int
    inpainting_fill: int
    restore_faces: bool
    tiling: bool
    n_iter: int
    batch_size: int
    cfg_scale: float
    denoising_strength: float
    seed: int
    subseed: int
    subseed_strength: float
    seed_resize_from_h: int
    seed_resize_from_w: int
    seed_enable_extras: bool
    height: int
    width: int
    resize_mode: int
    inpaint_full_res: bool
    inpaint_full_res_padding: int
    inpainting_mask_invert: int
    img2img_batch_input_dir: str
    img2img_batch_output_dir: str


@router.post("/api/txt2img")
def txt2img(payload: PayloadTxt2Img):
    _txt2img = import_module("modules.txt2img")

    images, info, _ = _txt2img.txt2img(
        payload.prompt,
        payload.negative_prompt,
        payload.prompt_style,
        payload.prompt_style2,
        payload.steps,
        payload.sampler_index,
        payload.restore_faces,
        payload.tiling,
        payload.n_iter,
        payload.batch_size,
        payload.cfg_scale,
        payload.seed,
        payload.subseed,
        payload.subseed_strength,
        payload.seed_resize_from_h,
        payload.seed_resize_from_w,
        payload.seed_enable_extras,
        payload.height,
        payload.width,
        payload.enable_hr,
        payload.denoising_strength,
        payload.firstphase_width,
        payload.firstphase_height,
        0
    )
    print(info)
    return {"images": images2base64(images)}


@router.post("/api/img2img")
def img2img(payload: PayloadImg2Img):
    _img2img = import_module("modules.img2img")

    images, info, _ = _img2img.img2img(
        payload.mode,
        payload.prompt,
        payload.negative_prompt,
        payload.prompt_style,
        payload.prompt_style2,
        payload.init_img,
        payload.init_img_with_mask,
        payload.init_img_inpaint,
        payload.init_mask_inpaint,
        payload.mask_mode,
        payload.steps,
        payload.sampler_index,
        payload.mask_blur,
        payload.inpainting_fill,
        payload.restore_faces,
        payload.tiling,
        payload.n_iter,
        payload.batch_size,
        payload.cfg_scale,
        payload.denoising_strength,
        payload.seed,
        payload.subseed,
        payload.subseed_strength,
        payload.seed_resize_from_h,
        payload.seed_resize_from_w,
        payload.seed_enable_extras,
        payload.height,
        payload.width,
        payload.resize_mode,
        payload.inpaint_full_res,
        payload.inpaint_full_res_padding,
        payload.inpainting_mask_invert,
        payload.img2img_batch_input_dir,
        payload.img2img_batch_output_dir,
        0
    )
    print(info)
    return {"images": images2base64(images)}
