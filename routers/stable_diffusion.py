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
