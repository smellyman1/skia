{
        'none_sources': [
            '<(skia_src_path)/opts/SkBitmapProcState_opts_none.cpp',
            '<(skia_src_path)/opts/SkBlitMask_opts_none.cpp',
            '<(skia_src_path)/opts/SkBlitRow_opts_none.cpp',
            '<(skia_src_path)/opts/SkBlurImage_opts_none.cpp',
            '<(skia_src_path)/opts/SkMorphology_opts_none.cpp',
            '<(skia_src_path)/opts/SkTextureCompression_opts_none.cpp',
            '<(skia_src_path)/opts/SkUtils_opts_none.cpp',
            '<(skia_src_path)/opts/SkXfermode_opts_none.cpp',
        ],

        'armv7_sources': [
            '<(skia_src_path)/opts/SkBitmapProcState_opts_arm.cpp',
            '<(skia_src_path)/opts/SkBlitMask_opts_arm.cpp',
            '<(skia_src_path)/opts/SkBlitRow_opts_arm.cpp',
            '<(skia_src_path)/opts/SkBlurImage_opts_arm.cpp',
            '<(skia_src_path)/opts/SkMorphology_opts_arm.cpp',
            '<(skia_src_path)/opts/SkTextureCompression_opts_arm.cpp',
            '<(skia_src_path)/opts/SkUtils_opts_arm.cpp',
            '<(skia_src_path)/opts/SkXfermode_opts_arm.cpp',
            '<(skia_src_path)/opts/memset.arm.S',
        ],
        'neon_sources': [
            '<(skia_src_path)/opts/SkBitmapProcState_arm_neon.cpp',
            '<(skia_src_path)/opts/SkBitmapProcState_matrixProcs_neon.cpp',
            '<(skia_src_path)/opts/SkBlitMask_opts_arm_neon.cpp',
            '<(skia_src_path)/opts/SkBlitRow_opts_arm_neon.cpp',
            '<(skia_src_path)/opts/SkBlurImage_opts_neon.cpp',
            '<(skia_src_path)/opts/SkMorphology_opts_neon.cpp',
            '<(skia_src_path)/opts/SkTextureCompression_opts_neon.cpp',
            '<(skia_src_path)/opts/SkXfermode_opts_arm_neon.cpp',
            '<(skia_src_path)/opts/memset16_neon.S',
            '<(skia_src_path)/opts/memset32_neon.S',
        ],
        'neon_fp16_sources': [
        ],
        'arm64_sources': [
            '<(skia_src_path)/opts/SkBitmapProcState_arm_neon.cpp',
            '<(skia_src_path)/opts/SkBitmapProcState_matrixProcs_neon.cpp',
            '<(skia_src_path)/opts/SkBitmapProcState_opts_arm.cpp',
            '<(skia_src_path)/opts/SkBlitMask_opts_arm.cpp',
            '<(skia_src_path)/opts/SkBlitMask_opts_arm_neon.cpp',
            '<(skia_src_path)/opts/SkBlitRow_opts_arm.cpp',
            '<(skia_src_path)/opts/SkBlitRow_opts_arm_neon.cpp',
            '<(skia_src_path)/opts/SkBlurImage_opts_arm.cpp',
            '<(skia_src_path)/opts/SkBlurImage_opts_neon.cpp',
            '<(skia_src_path)/opts/SkMorphology_opts_arm.cpp',
            '<(skia_src_path)/opts/SkMorphology_opts_neon.cpp',
            '<(skia_src_path)/opts/SkTextureCompression_opts_none.cpp',
            '<(skia_src_path)/opts/SkUtils_opts_none.cpp',
            '<(skia_src_path)/opts/SkXfermode_opts_arm.cpp',
            '<(skia_src_path)/opts/SkXfermode_opts_arm_neon.cpp',
        ],

        'mips_dsp_sources': [
            '<(skia_src_path)/opts/SkBitmapProcState_opts_mips_dsp.cpp',
            '<(skia_src_path)/opts/SkBlitMask_opts_none.cpp',
            '<(skia_src_path)/opts/SkBlitRow_opts_mips_dsp.cpp',
            '<(skia_src_path)/opts/SkBlurImage_opts_none.cpp',
            '<(skia_src_path)/opts/SkMorphology_opts_none.cpp',
            '<(skia_src_path)/opts/SkTextureCompression_opts_none.cpp',
            '<(skia_src_path)/opts/SkUtils_opts_none.cpp',
            '<(skia_src_path)/opts/SkXfermode_opts_none.cpp',
        ],

        'sse2_sources': [
            '<(skia_src_path)/opts/SkBitmapFilter_opts_SSE2.cpp',
            '<(skia_src_path)/opts/SkBitmapProcState_opts_SSE2.cpp',
            '<(skia_src_path)/opts/SkBlitRect_opts_SSE2.cpp',
            '<(skia_src_path)/opts/SkBlitRow_opts_SSE2.cpp',
            '<(skia_src_path)/opts/SkBlurImage_opts_SSE2.cpp',
            '<(skia_src_path)/opts/SkMorphology_opts_SSE2.cpp',
            '<(skia_src_path)/opts/SkTextureCompression_opts_none.cpp',
            '<(skia_src_path)/opts/SkUtils_opts_SSE2.cpp',
            '<(skia_src_path)/opts/SkXfermode_opts_SSE2.cpp',
            '<(skia_src_path)/opts/opts_check_x86.cpp',
        ],
        'ssse3_sources': [
            '<(skia_src_path)/opts/SkBitmapProcState_opts_SSSE3.cpp',
        ],
        'sse41_sources': [
            '<(skia_src_path)/opts/SkBlurImage_opts_SSE4.cpp',
            '<(skia_src_path)/opts/SkBlitRow_opts_SSE4.cpp',
        ],
        'avx_sources': [
            '<(skia_src_path)/opts/SkDummy_opts_AVX.cpp',
        ],
}
