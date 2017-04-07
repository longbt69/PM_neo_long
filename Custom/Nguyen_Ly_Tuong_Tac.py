bl_info = {
    "name": "Tinh Toan Neo",
    "author": "Cong Ty TNHH 1 MTV G6T",
    "version": (1, 0),
    "blender": (2, 78, 0),
    "location": "View3D > NEO",
    "description": "Nguyen Ly Gia Co - NEO",
    "warning": "",
    "wiki_url": "",
    "category": "NEO"}
    
import bpy
from bpy.props import *
from bpy.app.handlers import persistent
import math
from mpmath import *
from mathutils import Vector #3d cursor

# Set Default Value
arrChonLoai = [('CONG', 'Cong', ''),  #VD:('hinh_tron', 'Hình Tròn', 1)
                 ('TRU', 'Tru', ''),
                 ('NHAN', 'Nhan', ''),
                 ('CHIA', 'Chia', '')]
arrDieuKienLoKhoan = [('KHO', 'Khô', ''),('AM', 'Ẩm', '')]
arrLoaiDatDa = [('RAN', 'Rắn', ''),('YEU', 'Yếu', '')]
#arrNguyenLy = ['Default', '1.Nguyên lý Treo', '2.Nguyên lý Bản dầm', '3.Nguyên lý Gia cố', '4.Nguyên lý Nêm', '5.Nguyên lý tương tác'] 
# Lấy ra Scene Name của màn hình hiện tại (Các Nguyên lý) : Có  thể dùng chung biến nguyenLy
nguyenLy = bpy.context.screen.scene.name
nguyenLy_0 = bpy.context.screen.scene.name
nguyenLy_1 = bpy.context.screen.scene.name
nguyenLy_2 = bpy.context.screen.scene.name
nguyenLy_3 = bpy.context.screen.scene.name
nguyenLy_4 = bpy.context.screen.scene.name
nguyenLy_5 = bpy.context.screen.scene.name
#
#    Tab Panel NEO
#
class ToolPanel_NEO(bpy.types.Panel):
	bl_label = "Dữ liệu đầu vào của NEO"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "NEO"

	def draw(self, context):
		layout = self.layout
		scn = context.scene
		   
		box = layout.box()
		col = box.column()
		title_size = 0.8
		
		# screen window
		#if bpy.context.screen.scene.name == 'Scripting.001':

		# Scene
		if bpy.context.screen.scene.name[0] == '1':
			#todo
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'DuongKinhThepNeoDn_NL1')
			row.label("(m)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'KhaNangChiuKeoThepNeoRN_NL1')
			row.label("(MPa)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'DuongKinhLoKhoanDlk_NL1')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'LucDinhKetGiuaBeTongVaThanhNeo_NL1')
			row.label("(MPa)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'LucDinhKetGiuaBeTongVaDatDa_NL1')
			row.label("(MPa)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'DieuKienLoKhoan_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoLamViecCuaNeoDlv_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoLamViecCuaKhoaNeoDlvz_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoTapTrungUngSuatKeoK2_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoTapTrungUngSuatK1_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuDaiNeoNhoRaMatLoLk_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoQuaTaiNocLoNp_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoQuaTaiHongLoNph_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoDieuChinhChieuDaiKhoaNeoKz_NL1')
			row.label(" ")
			
		elif bpy.context.screen.scene.name[0] == '2':
			#todo
			print("Neo: NguyenLy2")
			
		elif bpy.context.screen.scene.name[0] == '3':
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'DuongKinhThepNeoDb_NL3')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ModulDanHoiThepNeoEb_NL3')
			row.label("(Mpa)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ModulDanHoiVuaXiMangEg_NL3')
			row.label("(Mpa)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'DuongKinhLoKhoanDh_NL3')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuDaiNeoL_NL3')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'KhoangCachNeoA_NL3')
			row.label("(m)")
		elif bpy.context.screen.scene.name[0] == '4':
			#todo
			print("Neo: NguyenLy4")
		elif bpy.context.screen.scene.name[0] == '5':
			#todo
			print("Neo: NguyenLy5")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'DuongKinhThepNeoDb_NL5')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'DuongKinhLoKhoanDh_NL5')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ModulDanHoiThepNeoEb_NL5')
			row.label("(MPa)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ModulDanHoiVuXiMangEg_NL5')
			row.label("(MPa)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuDaiNeoL_NL5')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'KhoangCachNeoA_NL5')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoPoissonNeo_NL5')
			row.label(" ")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoPoissonVuaNeo_NL5')
			row.label(" ")
		else:
			#todo
			print('Neo: Default')
        
#
#    Tab Panel Dat Da
#
class ToolPanel_DATDA(bpy.types.Panel):
	bl_label = "Dữ liệu đầu vào của Đất Đá"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "Đất Đá"

	def draw(self, context):
		layout = self.layout
		scn = context.scene
		#layout.prop(scn, 'MyCustomInt', icon='BLENDER', toggle=True)   
		#layout.prop(scn, 'ChonLoai')
		box = layout.box()
		col = box.column()
		title_size = 0.8
		
		if bpy.context.screen.scene.name[0] == '1': # Nguyên lý 1
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'TrongLuongTheTich_NL1')
			row.label("(T/m3)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'UngSuatKeoDatDaVach_NL1')
			row.label("(T/m3)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'UngSuatNenDatDaVach_NL1')
			row.label("(T/m3)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocMaSatTrong_NL1')
			row.label("(độ)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HoSoPoisson_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'LoaiDatDa_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoLuuBien_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoTapTrungUngSuatKeoK2_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoTapTrungUngSuatK1_NL1')
			row.label(" ")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuDayPhanLopTrungBinhB_NL1')
			row.label("(m)")
			
		elif bpy.context.screen.scene.name[0] == '2': # Nguyên lý 2
			print("Đất Đá - Nguyên Lý 2")
		elif bpy.context.screen.scene.name[0] == '3': # Nguyên lý 3
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'TrongLuongTheTich_NL3')
			row.label("(T/m3)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ModulDanHoiDaEr_NL3')
			row.label("(Mpa)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoPoisson_NL3')
			row.label(" ")
			
		elif bpy.context.screen.scene.name[0] == '4': # Nguyên lý 4
			#  Góc dốc
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocDoc_1_NL4') 
			row.label("(độ)")
			
			#  Góc phương vị của khe nứt
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocPhuongVi_1_NL4') 
			row.label("(độ)")
			
			#  Tên khe nứt
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'TenKheNut_1_NL4') 
			row.label(" ")
			
			#  Góc dốc
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocDoc_2_NL4') 
			row.label("(độ)")
			
			#  Góc phương vị của khe nứt
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocPhuongVi_2_NL4') 
			row.label("(độ)")
			
			#  Tên khe nứt
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'TenKheNut_2_NL4') 
			row.label(" ")
			
			#  Góc dốc
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocDoc_3_NL4') 
			row.label("(độ)")
			
			#  Góc phương vị của khe nứt
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocPhuongVi_3_NL4') 
			row.label("(độ)")
			
			#  Tên khe nứt
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'TenKheNut_3_NL4') 
			row.label(" ")
		elif bpy.context.screen.scene.name[0] == '5': # Nguyên lý 5	
			#Độ bền nén đơn trục
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'DoBenNenDonTruc_NL5') 
			row.label("(MPa)")
			
			#Modul đàn hồi Er
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ModulDanHoiEr_NL5') 
			row.label("(GPa)")
			
			#Hệ số Poisson
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoPoisson_NL5') 
			row.label(" ")
			
			#Áp lực nước ngầm Po
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ApLucNuocNgamPo_NL5') 
			row.label("(MPa)")
			
#
#    Tab Panel Cong Trinh Ngam
#
class ToolPanel_CongTrinhNgam(bpy.types.Panel):
	bl_label = "Dữ liệu đầu vào của Công Trình Ngầm"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "Công Trình Ngầm"

	def draw(self, context):
		layout = self.layout
		scn = context.scene
		
		box = layout.box()
		col = box.column()
		title_size = 0.8
		
		if bpy.context.screen.scene.name[0] == '1': # Nguyên lý 1
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuSauH_NL1')
			row.label("(m)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuRong2a_NL1')
			row.label("(m)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuCaoH1_NL1')
			row.label("(m)")
			
			row = layout.row()
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuCaoTuongLoH2_NL1')
			row.label("(m)")
						
		elif bpy.context.screen.scene.name[0] == '2': # Nguyên lý 2
			print("Cong Trinh Ngam - Nguyen Ly 2")
			
		elif bpy.context.screen.scene.name[0] == '3':
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuSauCTN_NL3')
			row.label("(m)")
			
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'BanKinhCTN_NL3')
			row.label("(m)")
			
		elif bpy.context.screen.scene.name[0] == '4':
			#  Góc dốc của Công trình ngầm
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocDoc_CongTrinhNgam_NL4') 
			row.label("(độ)")
			
			#  Góc phương vị của Công trình ngầm
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'GocPhuongVi_CongTrinhNgam_NL4') 
			row.label("(độ)")
			
			#  Chiều rộng của Công trình ngầm
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuRong_CongTrinhNgam_NL4') 
			row.label("(m)")
		elif bpy.context.screen.scene.name[0] == '5':
			#  Bán kính Ra
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'BanKinhRa_NL5') 
			row.label("(m)")
			
	
class initOutPut(bpy.types.Panel):
	bl_label = "Dữ liệu đầu ra"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS" #TOOL_PROPS
	bl_idname = "ui.output"
	bl_category = "Kết quả"
	resultCV = bpy.props.StringProperty()
		
	def draw(self, context):
		ob = context.object
		layout = self.layout
		scn = context.scene
		
		title_size = 0.8
		if bpy.context.screen.scene.name[0] == '1':
			# New box
			box = layout.box()
			col = box.column()
			
			row = layout.row()        
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'HeSoOnDinhDatDaVachNv_NL1')
			row.label(" ")
			
			row = layout.row()        
			row = col.split(percentage=title_size, align=True)
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row.prop(scn, 'HeSoOnDinhDatDaHongNh_NL1')
			row.label(" ")
			
			row = layout.row()  
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuCaoVomSupLoB_NL1')
			row.label("(m)")
			
			# New box
			box = layout.box()
			col = box.column()
			
			row = layout.row()        
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'KhaNangChiuLuc1ThanhNeoPn_NL1')
			row.label("(MN)")
			
			# New box
			box = layout.box()
			col = box.column()
			
			row = layout.row()        
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuDai1ThanhNeoNocLn_NL1')
			row.label("(m)")
			
			row = layout.row()        
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'MatDoNeoVachSn_NL1')
			row.label("(neo/m2)")
			
			row = layout.row()        
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'KhoangCachNeoVachA1_NL1')
			row.label("(m)")
			
			# New box
			box = layout.box()
			col = box.column()
			
			row = layout.row()        
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'ChieuDai1ThanhNeoHongLh_NL1')
			row.label("(m)")
			
			
			
			row = layout.row()        
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'MatDoNeoHongSh_NL1')
			row.label("(neo/m2)")
			
			row = layout.row()        
			#row.label(text="Hệ số ổn định đất đá vách Nv")
			row = col.split(percentage=title_size, align=True)
			row.prop(scn, 'KhoangCachNeoHongA2_NL1')
			row.label("(m)")
						
		elif bpy.context.screen.scene.name[0] == '2':
			print("Đầu ra - Nguyên lý 2")
			
		elif bpy.context.screen.scene.name[0] == '3':
			# New box
			#box = layout.box()
			#col = box.column()
			
			layout.prop(scn, 'ChonLoai')
					
			row = layout.row()
			layout.operator("ui_custom.result")
			
			row.prop(scn, 'OutBanKinh_NL3')
			
			#view = context.space_data
			#row = col.split(percentage=title_size, align=True)
			col = layout.column()
			row = layout.row()
			row.label(text="")
			row.label(text="TT sau khi Neo")
			row.label(text="TT trước khi Neo")
			row.label("ĐVT")    
			
			row = layout.row()        
			row.label(text="Ứng Suất pháp tuyến")
			row.prop(scn, 'UngSuatPhapTuyenSau_NL3')
			row.prop(scn, 'UngSuatPhapTuyenTruoc_NL3')
			row.label("(m)") 
			
			row = layout.row()        
			row.label(text="Ứng Suất pháp tuyến")
			row.prop(scn, 'UngSuatTiepTuyenSau_NL3')
			row.prop(scn, 'UngSuatTiepTuyenTruoc_NL3')
			row.label("(m)") 
							
			row = layout.row()        
			row.label(text="Biến dạng")
			row.prop(scn, 'BienDangSau_NL3')
			row.prop(scn, 'BienDangTruoc_NL3')
			row.label("(m)") 
			
			row = layout.row()        
			row.label(text="Chuyển vị")
			row.prop(scn, 'ChuyenViSau_NL3')
			row.prop(scn, 'ChuyenViTruoc_NL3')
			row.label("(m)") 
			
			row = layout.row()        
			row.label(text="Modul đàn hồi")
			row.prop(scn, 'ModulDanHoiSau_NL3')
			row.prop(scn, 'ModulDanHoiTruoc_NL3')
			row.label("(m)")
			bpy.app.handlers.scene_update_post.append(cb_scene_update)
			if bpy.context.screen.scene.name[0] == '1':
				EventWatcher.AddWatcher( EventWatcher( bpy.data.scenes[nguyenLy_1], "LoaiDatDa_NL1", CompareLocation, CompareLocationCallback, True ) )
			elif bpy.context.screen.scene.name[0] == '3':
				EventWatcher.AddWatcher( EventWatcher( bpy.data.scenes[nguyenLy_3], "cursor_location", CompareLocation, CompareLocationCallback, True ) )
				EventWatcher.AddWatcher( EventWatcher( bpy.data.scenes[nguyenLy_3], 'ChonLoai', CompareLocation, CompareLocationCallback, True ) )
			
		elif bpy.context.screen.scene.name[0] == '4':			
			# Thể tích khối NÊM
			row = layout.row()
			row.prop(scn, 'TheTich_KhoiNem_NL4')
			row.label("(m3)")
			
			row = layout.row()
			layout.operator("ui_custom.result")

#
#    KEt Qua Tinh: NEO - Dat Da - Cong Trinh Ngam
#
#scn = bpy.context.scene
class KetQuaTinh(bpy.types.Operator):
	bl_idname = "ui_custom.result"
	bl_label = "Cập nhật"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "NEO"
		
	def execute(self, context):
		#scn = context.scene
		scene = bpy.context.scene
		if bpy.context.screen.scene.name[0] == '3':
			# Delete Cylinder
			for ob in scene.objects:
				if ob.type == 'MESH' and ob.name.startswith("Cylinder"):
					ob.select = True
				else: 
					ob.select = False

			bpy.ops.object.delete()
			#END delete Cylinder
			
				#print(obj.name)
			calculator(0) # 0: ĐỂ VẼ HÌNH
		elif bpy.context.screen.scene.name[0] == '4':
			for ob in scene.objects:
				if ob.type == 'MESH' and ob.name.startswith("Circle"):
					ob.select = True
				else: 
					ob.select = False

			bpy.ops.object.delete()
			tinh_toan_NEM()
		#return
		return{'FINISHED'}

# Tính thể tích
def tinh_V():
	print(" tính V")
	
#Tính Toán NÊM cho Nguyên Lý 42
def tinh_toan_NEM():
	print("Tính toán NÊM")
	# Tạo Khối cầu tròn
	bpy.ops.mesh.primitive_circle_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	
	# Tạo Eclip theo Thông số Khe nứt 1
	bpy.ops.mesh.primitive_circle_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	gocPhuongVi_1 = bpy.data.scenes[nguyenLy_4].GocPhuongVi_1_NL4
	gocDoc_1 = bpy.data.scenes[nguyenLy_4].GocDoc_1_NL4
	if gocDoc_1 > 180:
		gocDoc_1 = gocDoc_1 % 180
	gocDoc_1 = gocDoc_1 * 2 / 180
	bpy.context.object.rotation_euler[2] = radians(gocPhuongVi_1)
	obj = bpy.context.object
	obj.dimensions = [gocDoc_1, 2, 0]
	
	bpy.ops.mesh.primitive_circle_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	gocPhuongVi_2 = bpy.data.scenes[nguyenLy_4].GocPhuongVi_2_NL4
	gocDoc_1 = bpy.data.scenes[nguyenLy_4].GocDoc_2_NL4
	if gocDoc_1 > 180:
		gocDoc_1 = gocDoc_1 % 180
	gocDoc_1 = gocDoc_1 * 2 / 180
	bpy.context.object.rotation_euler[2] = radians(gocPhuongVi_2)
	obj = bpy.context.object
	obj.dimensions = [gocDoc_1, 2, 0]

	bpy.ops.mesh.primitive_circle_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	gocPhuongVi_3 = bpy.data.scenes[nguyenLy_4].GocPhuongVi_3_NL4
	gocDoc_1 = bpy.data.scenes[nguyenLy_4].GocDoc_3_NL4
	if gocDoc_1 > 180:
		gocDoc_1 = gocDoc_1 % 180
	gocDoc_1 = gocDoc_1 * 2 / 180
	bpy.context.object.rotation_euler[2] = radians(gocPhuongVi_3)
	obj = bpy.context.object
	obj.dimensions = [gocDoc_1, 2, 0]
	
	bpy.ops.mesh.primitive_circle_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	gocPhuongVi_CTN = bpy.data.scenes[nguyenLy_4].GocPhuongVi_CongTrinhNgam_NL4
	bpy.context.object.rotation_euler[2] = radians(gocPhuongVi_CTN)
	obj = bpy.context.object
	bpy.context.object.scale[0] = 0
	#obj.dimensions = [0.5, 2, 0]

	
def calculator(type):
    #scn = bpy.context.scene
    #choise = scn['ChonLoai']
    choise = bpy.data.scenes[nguyenLy_3].ChonLoai
    #print(choise)
	
    if choise == 'CONG':
        pheptinhcong()
    elif choise == 'TRU':
        pheptinhtru()
    elif choise == 'NHAN':
        pheptinhnhan()
    else:
        pheptinhchia()
    # Tính bán kính
    cursor_location_x = bpy.context.scene.cursor_location.x  
    cursor_location_y = bpy.context.scene.cursor_location.y  
    #cursor_location_z = bpy.context.scene.cursor_location.z  
    r_cursor_lcation = float(math.sqrt(cursor_location_x * cursor_location_x + cursor_location_y * cursor_location_y),)
    #scn['OutLabel'] = str(round(r_cursor_lcation, 2))
    #scn['OutBanKinh_NL3'] = r_cursor_lcation
	
    bpy.data.scenes[nguyenLy_3].OutBanKinh_NL3 = r_cursor_lcation
    if type == 0: #vẽ hình khối
        #Vẽ đối tượng cylinder
        bpy.ops.mesh.primitive_cylinder_add(end_fill_type='NOTHING', view_align=False, enter_editmode=False, location=(0,0,0), radius=2, depth=5)#.modifier_add(type='SOLIDIFY')
        bpy.ops.object.modifier_add(type='SOLIDIFY')
#       bpy.ops.object.modifier_add(type='Solidify')
		# Set độ dày
        bpy.context.object.modifiers["Solidify"].thickness = 0.5
   
def toa_do():
    cursor_location_x = bpy.context.scene.cursor_location.x  
    cursor_location_y = bpy.context.scene.cursor_location.y  
    r_cursor_lcation = float(math.sqrt(cursor_location_x * cursor_location_x + cursor_location_y * cursor_location_y),)
    return r_cursor_lcation + 1.0

def pheptinhcong():
	bpy.data.scenes[nguyenLy_3].UngSuatPhapTuyenSau_NL3 = 1.0
	bpy.data.scenes[nguyenLy_3].UngSuatTiepTuyenSau_NL3 = 1.0
	bpy.data.scenes[nguyenLy_3].BienDangSau_NL3 = 1.0
	bpy.data.scenes[nguyenLy_3].ChuyenViSau_NL3 = 1.0
	bpy.data.scenes[nguyenLy_3].ModulDanHoiSau_NL3 = 1.0
	
	bpy.data.scenes[nguyenLy_3].UngSuatPhapTuyenTruoc_NL3 = 1.0
	bpy.data.scenes[nguyenLy_3].UngSuatTiepTuyenTruoc_NL3 = 1.0
	bpy.data.scenes[nguyenLy_3].BienDangTruoc_NL3 = 1.0
	bpy.data.scenes[nguyenLy_3].ChuyenViTruoc_NL3 = 1.0
	bpy.data.scenes[nguyenLy_3].ModulDanHoiTruoc_NL3 = 1.0

def pheptinhtru():
    print('tru')

def pheptinhnhan():
    print('nhan')

def pheptinhchia():
	print('chia')
    
def GET_Location_3D_Cursor():
    print("x : %s" % (bpy.context.scene.cursor_location.x))
    print("y : %s" % (bpy.context.scene.cursor_location.y))
    print("z : %s" % (bpy.context.scene.cursor_location.z))
    print("xyz : %s" % (bpy.context.scene.cursor_location.xyz))
    
''' DONG ket qua tra ve '''   

#A class that takes into account a context and one of its attributes value
#If the value changes a callback is fired
class EventWatcher:

    #Set of watchers
    eventWatchers = set()

    @staticmethod
    def AddWatcher( watcher ):
        EventWatcher.eventWatchers.add( watcher )    

    @staticmethod
    def RemoveWatcher( watcher ):
        EventWatcher.eventWatchers.remove( watcher )

    @staticmethod
    def RemoveAllWatchers():
        EventWatcher.eventWatchers.clear()

    #From 'context', 'path' needs to exist
    #'comparer' is to compare the previous value of context.path to its new value
    #'callback' is the cb called if the value if changed
    #'copyValue' indicates if the value needs to be copied (that can be needed as if not old and new value may point onto the same object)
    def __init__( self, context, path, comparer, callback, copyValue ):
        self.context = context
        self.path = path
        self.comparer = comparer
        self.callback = callback
        self.copyValue = copyValue
        self.currentValue = self.GetValue()

    def GetValue( self ):
        value = getattr( self.context, self.path )
        if self.copyValue and self.path  == 'cursor_location':
            value = value.copy()
        return value

    def Fire( self ):
        newValue = self.GetValue()
        if self.comparer( self.currentValue, newValue ) == False:
            self.callback( self, newValue )
            self.currentValue = newValue

#Global loop on the watchers. This callback responds to scene_update_post global handler
def cb_scene_update(context):
	#print('scene update')
	for ew in EventWatcher.eventWatchers:
		ew.Fire()

#Example:

#The comparaison (for cursor location, it is a vector comparison)
def CompareLocation( l1, l2 ):
    return l1 == l2

def changeEvent():
	if bpy.data.scenes[nguyenLy_1].LoaiDatDa_NL1 == 'RAN':
		bpy.data.scenes[nguyenLy_1].HeSoLuuBien_NL1 = 0.8
	else:
		bpy.data.scenes[nguyenLy_1].HeSoLuuBien_NL1 = 0.81
	
#The callback to execute when the cursor's location changes    
def CompareLocationCallback( watcher, newValue ):
	calculator(1)
	'''print(bpy.context.screen.scene.name[0])
	if bpy.context.screen.scene.name[0] == '1':
		changeEvent()
	elif bpy.context.screen.scene.name[0] == '3':
		calculator(1)'''
	#print( 'New value', newValue )
	
# excute
#bpy.app.handlers.scene_update_post.append(cb_scene_update)
#Install the watcher which will run the callback
#EventWatcher.AddWatcher( EventWatcher( bpy.data.scenes[0], "cursor_location", CompareLocation, CompareLocationCallback, True ) )
###########################################################

class NguyenLy4:
	'''# Khe nứt 1
	goc_doc_1
	goc_phuong_vi_1
	ten_khe_nut_1
	
	# Khe nứt 2
	goc_doc_2
	goc_phuong_vi_2
	ten_khe_nut_2
	
	# Khe nứt 3
	goc_doc_3
	goc_phuong_vi_3
	ten_khe_nut_3
	
	# Góc phương vị của Công trình ngầm
	goc_doc__cong_trinh_ngam
	goc_phuong_vi__cong_trinh_ngam
	chieu_rong_cong_trinh_ngam
	
	# thể tích khối NÊM
	the_tich_khoi_nem '''
	def __init__(self, gd_1, gpv_1, tkn_1, gd_2, gpv_2, tkn_2, gd_3, gpv_3, tkn_3, gd_ctn, gpv_ctn, cr_ctn, tt_khoi_nem):
		self.goc_doc_1 = gd1
		self.goc_phuong_vi_1 = gpv_1
		self.ten_khe_nut_1 = tkn_1
		
		self.goc_doc_2 = gd2
		self.goc_phuong_vi_2 = gpv_2
		self.ten_khe_nut_2 = tkn_2
		
		self.goc_doc_3 = gd3
		self.goc_phuong_vi_3 = gpv_3
		self.ten_khe_nut_3 = tkn_3
		
		self.goc_doc__cong_trinh_ngam = gd_ctn
		self.goc_phuong_vi__cong_trinh_ngam = gpv_ctn
		self.chieu_rong_cong_trinh_ngam = cr_ctn
		
		self.the_tich_khoi_nem = tt_khoi_nem
		
	
class RegisterParameter(bpy.types.PropertyGroup):
	### NGUYEN LY 1 ###
	# TO DO
	#-NEO
	duong_kinh_kheo_neo_Dn_NL1							= 0.02		#1	Đường kính thép neo	dn	m
	kha_nang_chiu_keo_thep_neo_RN_NL1					= 210.0		#2	Khả năng chịu kéo thép neo	Rn	MPa
	duong_kinh_lo_khoan_Dlk_NL1							= 0.04		#3	Đường kính lỗ khoan	dlk	m #
	luc_dinh_ket_giua_be_tong_va_thanh_neo_T1_NL1		= 50.0		#4	Lực dính kết giữa bê tông và thanh neo	1	MPa #
	luc_dinh_ket_giua_be_tong_va_dat_da_T2_NL1			= 40.0		#5	Lực dính kết giữa bê tông và đất đá	2	MPa
	dieu_kien_lo_khoan_NL1								= 'khô/ẩm'	#6	Điều kiện lỗ khoan	Khô/ẩm	-
	he_so_lam_viec_cua_neo_Dlv_NL1						= 0.9		#7	Hệ số làm việc của neo 	dlv	-
	he_so_lam_viec_cua_khoa_neo_Dlvz_NL1				= 0.0		#8	Hệ số làm việc của khóa neo 	dlvz	-
	he_so_tap_trung_ung_suat_keo_K2_NL1					= 0.0		#9	Hệ số tập trung ứng suất kéo 	k2	-
	he_so_tap_trung_ung_suat_K1_NL1						= 0.0		#10	Hệ số tập trung ứng suất	k1	-
	chieu_dai_neo_nho_ra_mat_lo_Lk_NL1					= 0.0		#11	Chiều dài neo nhô ra mặt lộ	Lk	-
	he_so_qua_tai_noc_lo_Np_NL1							= 0.0		#12	Hệ số quá tải nóc lò	np	-
	he_so_qua_tai_hong_lo_Nph_NL1						= 0.0		#13	Hệ số quá tải hông lò	nph	-
	he_so_dieu_chinh_chieu_dai_khoa_neo_Kz_NL1			= 0.0		#14	Hệ số điều chỉnh chiều dài khóa neo 	kz	-
	
	bpy.types.Scene.DuongKinhThepNeoDn_NL1				= FloatProperty(name = "Đường kính thép neo Dn", default = duong_kinh_kheo_neo_Dn_NL1)
	bpy.types.Scene.KhaNangChiuKeoThepNeoRN_NL1			= FloatProperty(name = "Khả năng chịu kéo thép neo Rn", default = kha_nang_chiu_keo_thep_neo_RN_NL1)
	bpy.types.Scene.DuongKinhLoKhoanDlk_NL1				= FloatProperty(name = "Đường kính lỗ khoan Dlk", default = duong_kinh_lo_khoan_Dlk_NL1)
	bpy.types.Scene.LucDinhKetGiuaBeTongVaThanhNeo_NL1	= FloatProperty(name = "Lực dính kết giữa bê tông và thanh neo", default = luc_dinh_ket_giua_be_tong_va_thanh_neo_T1_NL1)
	bpy.types.Scene.LucDinhKetGiuaBeTongVaDatDa_NL1		= FloatProperty(name = "Lực dính kết giữa bê tông và đất đá", default = luc_dinh_ket_giua_be_tong_va_dat_da_T2_NL1)
	bpy.types.Scene.DieuKienLoKhoan_NL1					= EnumProperty(name = "Điều kiện lỗ khoan(Khô/ẩm)", items = arrDieuKienLoKhoan) #default = dieu_kien_lo_khoan_NL1, 
	bpy.types.Scene.HeSoLamViecCuaNeoDlv_NL1			= FloatProperty(name = "Hệ số làm việc của neo Dlv", default = he_so_lam_viec_cua_neo_Dlv_NL1)
	bpy.types.Scene.HeSoLamViecCuaKhoaNeoDlvz_NL1		= FloatProperty(name = "Hệ số làm việc của khóa neo Dlvz", default = he_so_lam_viec_cua_khoa_neo_Dlvz_NL1)
	bpy.types.Scene.HeSoTapTrungUngSuatKeoK2_NL1		= FloatProperty(name = "Hệ số tập trung ứng suất kéo k2", default = he_so_tap_trung_ung_suat_keo_K2_NL1)
	bpy.types.Scene.HeSoTapTrungUngSuatK1_NL1			= FloatProperty(name = "Hệ số tập trung ứng suất k1", default = he_so_tap_trung_ung_suat_K1_NL1)
	bpy.types.Scene.ChieuDaiNeoNhoRaMatLoLk_NL1			= FloatProperty(name = "Chiều dài neo nhô ra mặt lộ Lk", default = chieu_dai_neo_nho_ra_mat_lo_Lk_NL1)
	bpy.types.Scene.HeSoQuaTaiNocLoNp_NL1				= FloatProperty(name = "Hệ số quá tải nóc lò Np", default = he_so_qua_tai_noc_lo_Np_NL1)
	bpy.types.Scene.HeSoQuaTaiHongLoNph_NL1				= FloatProperty(name = "Hệ số quá tải hông lò Nph", default = he_so_qua_tai_hong_lo_Nph_NL1)
	bpy.types.Scene.HeSoDieuChinhChieuDaiKhoaNeoKz_NL1	= FloatProperty(name = "Hệ số điều chỉnh chiều dài khóa neo Kz", default = he_so_dieu_chinh_chieu_dai_khoa_neo_Kz_NL1)

	#-DATDA
	trong_luong_the_tich_NL1							= 2.6		#1	Trọng lượng thể tích		T/m3
	ung_suat_keo_dat_da_NL1								= 781.0		#2	Ứng suất kéo đất đá vách	k	T/m2
	ung_suat_nen_dat_dat_vach_NL1						= 1910.0	#3	Ứng suất nén đất đá vách	n	T/m2
	goc_ma_sat_trong_NL1								= 30.0		#4	Góc ma sát trong		Độ
	he_so_Poisson_NL1									= 0.7		#5	Hệ số Poisson		- 
	loai_dat_da_NL1										= 'Rắn/Yếu'	#6	Loại đất đá	Rắn/Yếu	-
	he_so_luu_bien_NL1									= 0.8		#7	Hệ số lưu biến		-
	he_so_tap_trung_ung_suat_keo_K2_NL1					= 0.5		#8	Hệ số tập trung ứng suất kéo	k2	-
	he_so_tap_trung_ung_suat_K1_NL1						= 0.0		#9	Hệ số tập trung ứng suất	k1	-
	chieu_day_phan_lop_trung_binh_B_NL1					= 1.6		#10	Chiều dày phân lớp trung bình	b	m

	bpy.types.Scene.TrongLuongTheTich_NL1				= FloatProperty(name = "Trọng lượng thể tích", default = trong_luong_the_tich_NL1)
	bpy.types.Scene.UngSuatKeoDatDaVach_NL1				= FloatProperty(name = "Ứng suất kéo đất đá vách", default = ung_suat_keo_dat_da_NL1)
	bpy.types.Scene.UngSuatNenDatDaVach_NL1				= FloatProperty(name = "Ứng suất nén đất đá vách", default = ung_suat_nen_dat_dat_vach_NL1)
	bpy.types.Scene.GocMaSatTrong_NL1					= FloatProperty(name = "Góc ma sát trong", default = goc_ma_sat_trong_NL1)
	bpy.types.Scene.HoSoPoisson_NL1						= FloatProperty(name = "Hệ số Poisson", default = he_so_Poisson_NL1)
	bpy.types.Scene.LoaiDatDa_NL1						= EnumProperty(name = "Loại đất đá (Rắn/Yếu)", items = arrLoaiDatDa) #, default = loai_dat_da_NL1
	bpy.types.Scene.HeSoLuuBien_NL1						= FloatProperty(name = "Hệ số lưu biến", default = he_so_luu_bien_NL1)
	bpy.types.Scene.HeSoTapTrungUngSuatKeoK2_NL1		= FloatProperty(name = "Hệ số tập trung ứng suất kéo K2", default = he_so_tap_trung_ung_suat_keo_K2_NL1)
	bpy.types.Scene.HeSoTapTrungUngSuatK1_NL1			= FloatProperty(name = "Hệ số tập trung ứng suất K1", default = he_so_tap_trung_ung_suat_K1_NL1)
	bpy.types.Scene.ChieuDayPhanLopTrungBinhB_NL1		= FloatProperty(name = "Chiều dày phân lớp trung bình B", default = chieu_day_phan_lop_trung_binh_B_NL1)

	#-Cong trinh ngam
	chieu_sau_H_NL1										= 120.0		#1	Chiều sâu 	H	m
	chieu_rong_2a_NL1									= 3.0		#2	Chiều rộng 	2a	m
	chieu_cao_H1_NL1									= 2.0		#3	Chiều cao	h1	m
	chieu_cao_tuong_lo_H2_NL1							= 0.0		#4	Chiều cao tường lò	h2	m
	
	bpy.types.Scene.ChieuSauH_NL1						= FloatProperty(name = "Chiều sâu H", default = chieu_sau_H_NL1)
	bpy.types.Scene.ChieuRong2a_NL1						= FloatProperty(name = "Chiều rộng 2a", default = chieu_rong_2a_NL1)
	bpy.types.Scene.ChieuCaoH1_NL1						= FloatProperty(name = "Chiều cao h1", default = chieu_cao_H1_NL1)
	bpy.types.Scene.ChieuCaoTuongLoH2_NL1				= FloatProperty(name = "Chiều cao tường lò h2", default = chieu_cao_tuong_lo_H2_NL1)
	
	# Đầu ra Nguyên Lý 1
	he_so_on_dinh_dat_da_vach_Nv_NL1					= 10.81		#1	Hệ số ổn định đất đá vách	nv	-
	he_so_on_dinh_dat_da_hong_Nh_NL1					= 2.20		#2	Hệ số ổn định đất đá hông	nh	-
	chieu_cao_vom_sup_lo_B_NL1							= 0.43		#3	Chiều cao vòm sụp lở	b	m
	kha_nang_chiu_luc_1_thanh_neo_Pn_NL1				= 0.88		#4	Khả năng chịu lực 1 thanh neo	Pn	MN
	chieu_dai_1_thanh_neo_noc_Ln_NL1					= 1.43		#5	Chiều dài 1 thanh neo nóc	Ln	m
	chieu_dai_1_thanh_neo_hong_Lh_NL1					= 0.82		#6	Chiều dài 1 thanh neo hông	Lh	m
	mat_do_neo_vach_Sn_NL1								= 1.50		#7	Mật độ neo vách	Sn	neo/m2
	khoang_cach_neo_vach_A1_NL1							= 0.82		#8	Khoảng cách neo vách	a1	m
	mat_do_neo_hong_Sh_NL1								= 1.15		#9	Mật độ neo hông	Sh	neo/m2
	khoang_cach_neo_hong_A2_NL1							= 0.93		#10	Khoảng cách neo hông	a2	m
	
	bpy.types.Scene.HeSoOnDinhDatDaVachNv_NL1			= FloatProperty(name = "Hệ số ổn định đất đá vách Nv", default = he_so_on_dinh_dat_da_vach_Nv_NL1)
	bpy.types.Scene.HeSoOnDinhDatDaHongNh_NL1			= FloatProperty(name = "Hệ số ổn định đất đá hông Nh", default = he_so_on_dinh_dat_da_hong_Nh_NL1)
	bpy.types.Scene.ChieuCaoVomSupLoB_NL1				= FloatProperty(name = "Chiều cao vòm sụp lở B", default = chieu_cao_vom_sup_lo_B_NL1)
	bpy.types.Scene.KhaNangChiuLuc1ThanhNeoPn_NL1		= FloatProperty(name = "Khả năng chịu lực 1 thanh neo Pn", default = kha_nang_chiu_luc_1_thanh_neo_Pn_NL1)
	bpy.types.Scene.ChieuDai1ThanhNeoNocLn_NL1			= FloatProperty(name = "Chiều dài 1 thanh neo nóc Ln", default = chieu_dai_1_thanh_neo_noc_Ln_NL1)
	bpy.types.Scene.ChieuDai1ThanhNeoHongLh_NL1			= FloatProperty(name = "Chiều dài 1 thanh neo hông Lh", default = chieu_dai_1_thanh_neo_hong_Lh_NL1)
	bpy.types.Scene.MatDoNeoVachSn_NL1					= FloatProperty(name = "Mật độ neo vách Sn", default = mat_do_neo_vach_Sn_NL1)
	bpy.types.Scene.KhoangCachNeoVachA1_NL1				= FloatProperty(name = "Khoảng cách neo vách A1", default = khoang_cach_neo_vach_A1_NL1)
	bpy.types.Scene.MatDoNeoHongSh_NL1					= FloatProperty(name = "Mật độ neo hông Sh", default = mat_do_neo_hong_Sh_NL1)
	bpy.types.Scene.KhoangCachNeoHongA2_NL1				= FloatProperty(name = "Khoảng cách neo hông A2", default = khoang_cach_neo_hong_A2_NL1)

	###### END NGUYEN LY 1 #####
	##########################################################################################
	
	### NGUYEN LY 2 ###
	# TO DO
	###### END NGUYEN LY 2 #####
	
	##########################################################################################
	
	### NGUYEN LY 3 ###
	#-NEO
	duong_kinh_kheo_neo_Db_NL3							= 0.02
	modul_dan_hoi_thep_neo_Eb_NL3						= 296.8263
	modul_dan_hoi_vua_xi_mang_Eg_NL3					= 54.5982
	duong_kinh_lo_khoan_Dh_NL3							= 0.036
	chieu_dai_neo_L_NL3									= 1.5
	khoang_cach_neo_A_NL3								= 0.8

	#-DATDA
	trong_luong_the_tich_NL3							= 2.6
	modul_dan_hoi_da_Er_NL3								= 48.7678
	he_so_Poisson_NL3									= 0.7

	#-Cong trinh ngam
	chieu_sau_CTN_NL3									= 160.0
	ban_kinh_CTN_NL3									= 3.0
	
	# Bán kinh đầu vào(tích điểm)
	out_ban_kinh_NL3									= 1.02

	#-Sau
	ung_suat_phap_tuyen_sau_NL3							= 356.95
	ung_suat_tiep_tuyen_sau_NL3							= 475.52
	bien_dang_sau_NL3									= 1.82
	chuyen_vi_sau_NL3									= 130.43
	modul_dan_hoi_sau_NL3								= 48.77

	#-Truoc
	ung_suat_phap_tuyen_truoc_NL3						= 161.18
	ung_suat_tiep_tuyen_truoc_NL3						= 789.42
	bien_dang_truoc_NL3									= 2.5
	chuyen_vi_truoc_NL3									= 163.17
	modul_dan_hoi_truoc_NL3								= 48.77
	
	###END Set Default Value
	bpy.types.Scene.DuongKinhThepNeoDb_NL3				= FloatProperty(name = "Đường kính thép Neo Db", default = duong_kinh_kheo_neo_Db_NL3)
	bpy.types.Scene.ModulDanHoiThepNeoEb_NL3			= FloatProperty(name = "Modul đàn hồi thép Neo Eb", default = modul_dan_hoi_thep_neo_Eb_NL3)
	bpy.types.Scene.ModulDanHoiVuaXiMangEg_NL3			= FloatProperty(name = "Modul đàn hồi vữa xi măng Eg", default = modul_dan_hoi_vua_xi_mang_Eg_NL3)
	bpy.types.Scene.DuongKinhLoKhoanDh_NL3				= FloatProperty(name = "Đường kinh lỗ khoan (Dh)", default = duong_kinh_lo_khoan_Dh_NL3)
	bpy.types.Scene.ChieuDaiNeoL_NL3					= FloatProperty(name = "Chiều dài Neo L", default = chieu_dai_neo_L_NL3)
	bpy.types.Scene.KhoangCachNeoA_NL3					= FloatProperty(name = "Khoảng cách Neo (a)", default = khoang_cach_neo_A_NL3)
	#END NEO
	
	#DATDA
	bpy.types.Scene.TrongLuongTheTich_NL3				= FloatProperty(name = "Trọng lượng thể tích", default = trong_luong_the_tich_NL3)    
	bpy.types.Scene.ModulDanHoiDaEr_NL3					= FloatProperty(name = "Modul đàn hồi đá Er", default = modul_dan_hoi_da_Er_NL3)
	bpy.types.Scene.HeSoPoisson_NL3						= FloatProperty(name = "Hệ số Poisson", default = he_so_Poisson_NL3)
	##END DATDA
	
	#Cong Trinh Ngam
	bpy.types.Scene.ChieuSauCTN_NL3						= FloatProperty(name = "Chiều sâu CTN", default = chieu_sau_CTN_NL3)
	bpy.types.Scene.BanKinhCTN_NL3						= FloatProperty(name = "Bán kính CTN", default = ban_kinh_CTN_NL3)
	##END Cong Trinh Ngam

	#Result
	bpy.types.Scene.ChonLoai							= EnumProperty(items = arrChonLoai, name = "Chọn loại") #, default = 0 -> lỗi set default 
	bpy.types.Scene.OutBanKinh_NL3						= FloatProperty(name = "Bán kính", default = out_ban_kinh_NL3)
		
	# Sau
	bpy.types.Scene.UngSuatPhapTuyenSau_NL3				= FloatProperty(name='', default = ung_suat_phap_tuyen_sau_NL3)
	bpy.types.Scene.UngSuatTiepTuyenSau_NL3				= FloatProperty(name='', default = ung_suat_tiep_tuyen_sau_NL3)
	bpy.types.Scene.BienDangSau_NL3						= FloatProperty(name='', default = bien_dang_sau_NL3)
	bpy.types.Scene.ChuyenViSau_NL3						= FloatProperty(name='', default = chuyen_vi_sau_NL3)
	bpy.types.Scene.ModulDanHoiSau_NL3					= FloatProperty(name='', default = modul_dan_hoi_sau_NL3)
	
	# Trước
	bpy.types.Scene.UngSuatPhapTuyenTruoc_NL3			= FloatProperty(name='', default = ung_suat_phap_tuyen_truoc_NL3)
	bpy.types.Scene.UngSuatTiepTuyenTruoc_NL3			= FloatProperty(name='', default = ung_suat_tiep_tuyen_truoc_NL3)
	bpy.types.Scene.BienDangTruoc_NL3					= FloatProperty(name='', default = bien_dang_truoc_NL3)
	bpy.types.Scene.ChuyenViTruoc_NL3					= FloatProperty(name='', default = chuyen_vi_truoc_NL3)
	bpy.types.Scene.ModulDanHoiTruoc_NL3				= FloatProperty(name='', default = modul_dan_hoi_truoc_NL3)
	##END Result
	###### END NGUYEN LY 3 #####
	
	##########################################################################################
	
	### NGUYEN LY 4 ###
	# Default Khe nứt 1
	goc_doc_1_NL4										= 45.0		 # Góc dốc
	goc_phuong_vi_1_NL4									= 180.0		 # Góc phương vị của khe nứt
	ten_khe_nut_1_NL4									= 'Khe nứt 1'# Tên khe nứt
	
	# Default Khe nứt 2
	goc_doc_2_NL4										= 45.0		 #  Góc dốc
	goc_phuong_vi_2_NL4									= 60.0		 # Góc phương vị của khe nứt
	ten_khe_nut_2_NL4									= 'Khe nứt 2'# Tên khe nứt
	
	# Default Khe nứt 3
	goc_doc_3_NL4										= 45.0		 #  Góc dốc
	goc_phuong_vi_3_NL4									= 300.0		 # Góc phương vị của khe nứt
	ten_khe_nut_3_NL4									= 'Khe nứt 3'# Tên khe nứt
	
	# Default góc phương vị của Công trình ngầm
	goc_doc__cong_trinh_ngam_NL4						= 0			 # Góc dốc của Công trình ngầm
	goc_phuong_vi__cong_trinh_ngam_NL4					= 45.0		 # Góc phương vị của Công trình ngầm
	chieu_rong_cong_trinh_ngam_NL4						= 4			 # Góc dốc của Công trình ngầm
	
	# Default thể tích khối NÊM
	the_tich_khoi_nem_NL4								= 0.0		 # Góc dốc của Công trình ngầm
	
	bpy.types.Scene.GocDoc_1_NL4						= FloatProperty(name='Góc dốc 1', default = goc_doc_1_NL4)
	bpy.types.Scene.GocPhuongVi_1_NL4					= FloatProperty(name='Góc phương vị 1', default = goc_phuong_vi_1_NL4)
	bpy.types.Scene.TenKheNut_1_NL4						= StringProperty(name='Tên khe nứt 1', default = ten_khe_nut_1_NL4)
	
	bpy.types.Scene.GocDoc_2_NL4						= FloatProperty(name='Góc dốc 2', default = goc_doc_2_NL4)
	bpy.types.Scene.GocPhuongVi_2_NL4					= FloatProperty(name='Góc phương vị 2', default = goc_phuong_vi_2_NL4)
	bpy.types.Scene.TenKheNut_2_NL4						= StringProperty(name='Tên khe nứt 2', default = ten_khe_nut_2_NL4)
	
	bpy.types.Scene.GocDoc_3_NL4						= FloatProperty(name='Góc dốc 3', default = goc_doc_3_NL4)
	bpy.types.Scene.GocPhuongVi_3_NL4					= FloatProperty(name='Góc phương vị 3', default = goc_phuong_vi_3_NL4)
	bpy.types.Scene.TenKheNut_3_NL4						= StringProperty(name='Tên khe nứt 3', default = ten_khe_nut_3_NL4)
	
	bpy.types.Scene.GocDoc_CongTrinhNgam_NL4			= FloatProperty(name='Góc dốc', default = goc_doc__cong_trinh_ngam_NL4)
	bpy.types.Scene.GocPhuongVi_CongTrinhNgam_NL4		= FloatProperty(name='Góc phương vị', default = goc_phuong_vi__cong_trinh_ngam_NL4)
	bpy.types.Scene.ChieuRong_CongTrinhNgam_NL4			= FloatProperty(name='Chiều rộng', default = chieu_rong_cong_trinh_ngam_NL4)
	
	# Thể tích khối NÊM
	bpy.types.Scene.TheTich_KhoiNem_NL4					= FloatProperty(name='Thể tích khối NÊM', default = the_tich_khoi_nem_NL4)
	###### END NGUYEN LY 4 #####
	
	##########################################################################################
	
	### NGUYEN LY 5 ###
	# TO DO
	# NEO
	duong_kinh_theo_neo_db_NL5							= 0.0			 #1	Đường kính thép neo	db	m
	duong_kinh_lo_khoan_Dh_NL5							= 0.0			 #2	Đường kính lỗ khoan	dh	m
	modul_dan_hoi_thep_neo_Eb_NL5						= 210.0			 #3	Modul đàn hồi thép neo	Eb	MPa
	modul_dan_hoi_vua_xi_mang__NL5						= 0.0			 #4	Modul đàn hồi vữa xi măng 	Eg	MPa
	chieu_dai_neo_L_NL5									= 4.0			 #5	Chiều dài neo	L	m
	khoang_cach_neo_A_NL5								= 0.0			 #6	Khoảng cách neo	a	m
	he_so_Poisson_neo_NL5								= 0.35			 #7	Hệ số Poisson neo	b	-
	he_so_Poisson_vua_neo_NL5							= 0.35			 #8	Hệ số Poisson vữa neo	g	-
	
	
	bpy.types.Scene.DuongKinhThepNeoDb_NL5				= FloatProperty(name='Đường kính thép neo Db', default = duong_kinh_theo_neo_db_NL5)
	bpy.types.Scene.DuongKinhLoKhoanDh_NL5				= FloatProperty(name='Đường kính lỗ khoan Dh', default = duong_kinh_lo_khoan_Dh_NL5)
	bpy.types.Scene.ModulDanHoiThepNeoEb_NL5			= FloatProperty(name='Modul đàn hồi thép neo Eb', default = modul_dan_hoi_thep_neo_Eb_NL5)
	bpy.types.Scene.ModulDanHoiVuXiMangEg_NL5			= FloatProperty(name='Modul đàn hồi vữa xi măng Eg', default = modul_dan_hoi_vua_xi_mang__NL5)
	bpy.types.Scene.ChieuDaiNeoL_NL5					= FloatProperty(name='Chiều dài neo L', default = chieu_dai_neo_L_NL5)
	bpy.types.Scene.KhoangCachNeoA_NL5					= FloatProperty(name='Khoảng cách neo A', default = khoang_cach_neo_A_NL5)
	bpy.types.Scene.HeSoPoissonNeo_NL5					= FloatProperty(name='Hệ số Poisson neo', default = he_so_Poisson_neo_NL5)
	bpy.types.Scene.HeSoPoissonVuaNeo_NL5				= FloatProperty(name='Hệ số Poisson vữa neo', default = he_so_Poisson_vua_neo_NL5)
	
	# Đất Đá
	do_ben_nen_don_truc_NL5								= 0.5			 #1	Độ bền nén đơn trục	c	MPa
	modul_dan_hoi_Er_NL5								= 0.5			 #2	Modul đàn hồi	Er	GPa
	he_so_Poisson_NL5									= 0.35			 #3	Hệ số Poisson		- 
	ap_luc_nuoc_ngam_Po_NL5								= 1.0			 #4	Áp lực nước ngầm	Po	MPa
	
	bpy.types.Scene.DoBenNenDonTruc_NL5					= FloatProperty(name='Độ bền nén đơn trục', default = do_ben_nen_don_truc_NL5)
	bpy.types.Scene.ModulDanHoiEr_NL5					= FloatProperty(name='Modul đàn hồi Er', default = modul_dan_hoi_Er_NL5)
	bpy.types.Scene.HeSoPoisson_NL5						= FloatProperty(name='Hệ số Poisson', default = he_so_Poisson_NL5)
	bpy.types.Scene.ApLucNuocNgamPo_NL5					= FloatProperty(name='Áp lực nước ngầm Po', default = ap_luc_nuoc_ngam_Po_NL5)
	
	# Công Trình Ngầm
	ban_kinh_Ra_NL5										= 0.0			 #1	Bán kính 	Ra	m
	
	bpy.types.Scene.BanKinhRa_NL5						= FloatProperty(name='Bán kính Ra', default = ban_kinh_Ra_NL5)

	# Đầu ra
	
	###### END NGUYEN LY 5 #####
	
	#NEO
	'''del bpy.types.Scene.DuongKinhThepNeoDb_NL3
	del bpy.types.Scene.ModulDanHoiThepNeoEb_NL3
	del bpy.types.Scene.ModulDanHoiVuaXiMangEg_NL3
	del bpy.types.Scene.DuongKinhLoKhoanDh_NL3
	del bpy.types.Scene.ChieuDaiNeoL_NL3
	del bpy.types.Scene.KhoangCachNeoA_NL3
	##END NEO
	
	del bpy.types.Scene.TrongLuongTheTich_NL3
	del bpy.types.Scene.ModulDanHoiDaEr_NL3
	del bpy.types.Scene.HeSoPoisson_NL3
	##END DATDA
	
	#Cong Trinh Ngam
	del bpy.types.Scene.ChieuSauCTN_NL3    
	del bpy.types.Scene.BanKinhCTN_NL3
	##END Cong Trinh Ngam

	#Result
	del bpy.types.Scene.ChonLoai
	del bpy.types.Scene.OutBanKinh_NL3
	# Sau
	del bpy.types.Scene.UngSuatPhapTuyenSau_NL3
	del bpy.types.Scene.UngSuatTiepTuyenSau_NL3    
	del bpy.types.Scene.BienDangSau_NL3
	del bpy.types.Scene.ChuyenViSau_NL3
	del bpy.types.Scene.ModulDanHoiSau_NL3

	# Trước
	del bpy.types.Scene.UngSuatPhapTuyenTruoc_NL3
	del bpy.types.Scene.UngSuatTiepTuyenTruoc_NL3
	del bpy.types.Scene.BienDangTruoc_NL3
	del bpy.types.Scene.ChuyenViTruoc_NL3
	del bpy.types.Scene.ModulDanHoiTruoc_NL3'''
	##END Result
	
def register():
	#bpy.utils.register_module(__name__)
	bpy.utils.register_class(RegisterParameter)
	bpy.utils.register_class(ToolPanel_NEO)
	bpy.utils.register_class(ToolPanel_DATDA)
	bpy.utils.register_class(ToolPanel_CongTrinhNgam)
	bpy.utils.register_class(initOutPut)
	bpy.utils.register_class(KetQuaTinh)

def unregister():
	#bpy.utils.unregister_module(__name__)
	bpy.utils.unregister_class(RegisterParameter)
	bpy.utils.unregister_class(ToolPanel_NEO)
	bpy.utils.unregister_class(ToolPanel_DATDA)
	bpy.utils.unregister_class(ToolPanel_CongTrinhNgam)
	bpy.utils.unregister_class(initOutPut)
	bpy.utils.unregister_class(KetQuaTinh)
	
#    return
if __name__ == "__main__":
	register()
