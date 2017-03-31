import bpy
op = bpy.context.active_operator

op.AutoUpdate = True
op.SphereMesh = False
op.SmoothMesh = False
op.Subdivision = 20
op.MeshSize = 2.0
op.XOffset = 0.0
op.YOffset = 0.0
op.RandomSeed = 138
op.NoiseSize = 1.0
op.NoiseType = 'multi_fractal'
op.BasisType = '1'
op.VLBasisType = '0'
op.Distortion = 1.0
op.HardNoise = False
op.NoiseDepth = 8
op.mDimension = 1.0
op.mLacunarity = 2.0
op.mOffset = 1.0
op.mGain = 1.0
op.MarbleBias = '0'
op.MarbleSharp = '0'
op.MarbleShape = '0'
op.Invert = False
op.Height = 0.75
op.Offset = -0.25
op.Falloff = '1'
op.Sealevel = 0.0
op.Plateaulevel = 1.0
op.Strata = 5.0
op.StrataType = '0'
