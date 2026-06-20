<!-- PHIÊN BẢN CẬP NHẬT 06/2026: Bản markdown này đã được nâng cấp và phản ánh chính xác kiến trúc mới nhất PhoBERT Text-only + MLP (Hệ thống ShieldAI). Các số liệu tham chiếu: F1 93,71%, ROC-AUC 98,50%. Mọi yếu tố thuộc về phiên bản Hybrid cũ đã được loại bỏ. -->

<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 7.3.7.2 (Linux)"/>
	<meta name="author" content="Un-named"/>
	<meta name="created" content="2026-03-25T04:01:00"/>
	<meta name="changedby" content="Microsoft Office User"/>
	<meta name="changed" content="2026-03-25T04:09:00"/>
	<meta name="AppVersion" content="16.0000"/>
	<style type="text/css">
		* {
			color: black !important;
		}
		@page { 
			size: 210mm 297mm; 
			margin-left: 3cm; 
			margin-right: 1.5cm; 
			margin-top: 2cm; 
			margin-bottom: 2cm;
			@bottom-center {
				content: counter(page);
				font-family: "Times New Roman", serif;
				font-size: 11pt;
			}
		}
		p { line-height: 115%; orphans: 2; widows: 2; margin-bottom: 0.1in; direction: ltr; background: transparent }
		h1 { color: #000080; font-size: 14pt; font-weight: bold; text-align: left; orphans: 2; widows: 2; margin-top: 0.25in; margin-bottom: 0.14in; direction: ltr; background: transparent }
		h2 { color: #000080; font-weight: bold; text-align: left; orphans: 2; widows: 2; margin-bottom: 0.11in; direction: ltr; background: transparent }
		h3 { color: #000000; font-size: 12pt; font-weight: bold; text-align: left; orphans: 2; widows: 2; margin-top: 0.14in; margin-bottom: 0.06in; direction: ltr; background: transparent }
		a:link { color: #0563c1; text-decoration: underline }
		table, pre, img, figure { page-break-inside: avoid; break-inside: avoid; }
		h1, h2, h3, h4 { page-break-after: avoid; break-after: avoid; }
	</style>
</head>
<body lang="en-VN" link="#0563c1" vlink="#800000" dir="ltr"><p align="center" style="line-height: 100%; margin-bottom: 0.06in">
<font color="#000000"><font size="4" style="font-size: 14pt"><b>BỘ GIÁO DỤC VÀ ĐÀO TẠO</b></font></font></p>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in"><font color="#000000"><font size="4" style="font-size: 16pt"><b>TRƯỜNG
ĐẠI HỌC</b></font></font><font color="#000000"><font size="4" style="font-size: 16pt"><span lang="vi-VN"><b>
TÂN TẠO</b></span></font></font></p>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in"><font color="#000000"><font size="4" style="font-size: 14pt"><b>KHOA
CÔNG</b></font></font><font color="#000000"><font size="4" style="font-size: 14pt"><span lang="vi-VN"><b> NGHỆ
THÔNG TIN</b></span></font></font></p>
<p align="center" style="line-height: 100%; margin-bottom: 0in"><img src="Mau_Luan_Van_Tot_Nghiep_html_cf243cb600b36d28.png" name="Picture 1" align="bottom" width="180" height="206" border="0"/>
</p>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in"><font color="#000000"><font size="5" style="font-size: 22pt"><b>TIỂU LUẬN TỐT NGHIỆP ĐẠI HỌC</b></font></font></p>

<p align="center" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000"><font size="5" style="font-size: 18pt"><b>NGHIÊN CỨU, XÂY DỰNG CÔNG CỤ PHÂN TÍCH VÀ PHÁT HIỆN TIN GIẢ<br/>TIẾNG VIỆT BẰNG PHOBERT VÀ MẠNG NƠ-RON ĐA TẦNG<br/>(Hệ thống ShieldAI)</b></font></font></p>
<table width="100%" cellpadding="10" cellspacing="0" style="display: table; width: 100%; border-collapse: collapse; max-width: 600px; margin: 0 auto;">
	<col width="40%"/>
	<col width="60%"/>
	<tr valign="top">
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000"><b>Ngành:</b></font></p>
		</td>
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000">Khoa Học Máy Tính</font></p>
		</td>
	</tr>
	<tr valign="top">
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000"><b>Mã số:</b></font></p>
		</td>
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000">7480101</font></p>
		</td>
	</tr>
	<tr valign="top">
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000"><b>Khóa:</b></font></p>
		</td>
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000">2022</font></p>
		</td>
	</tr>
</table>
<table width="100%" cellpadding="10" cellspacing="0" style="display: table; width: 100%; border-collapse: collapse; max-width: 600px; margin: 0 auto;">
	<col width="40%"/>
	<col width="60%"/>
	<tr valign="top">
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000"><b>Sinh viên thực hiện:</b></font></p>
		</td>
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000">Hà Minh Chiến</font></p>
		</td>
	</tr>
	<tr valign="top">
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000"><b>Mã số sinh viên:</b></font></p>
		</td>
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000">2202095</font></p>
		</td>
	</tr>
	<tr valign="top">
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000"><b>Giảng viên hướng dẫn:</b></font></p>
		</td>
		<td style="border: 1px solid #d3d3d3; padding: 10px;"><p style="orphans: 0; widows: 0">
			<font color="#000000">Thầy Trần Ngọc Anh</font></p>
		</td>
	</tr>
</table>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in"><font color="#000000"><b>TÂY</b></font><font color="#000000"><span lang="vi-VN"><b>
NINH</b></span></font><font color="#000000"><b>, THÁNG 06 NĂM
2026</b></font></p>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in; page-break-before: always">
<font color="#000000"><font size="4" style="font-size: 14pt"><b>TRANG
PHÊ DUYỆT</b></font></font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">Luận
văn đã được trình và bảo vệ trước Hội đồng chấm
tiểu luận tốt nghiệp.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">Ngày
bảo vệ: ....../....../2026</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">Kết
quả: ....../10 điểm</font></p>
<table width="100%" cellpadding="10" cellspacing="0" style="display: table; width: 100%; table-layout: fixed; border-collapse: collapse; border: 1px solid #d3d3d3; margin-top: 30px; margin-bottom: 30px;">
	<col width="50%"/>
	<col width="50%"/>
	<tr valign="top">
		<td style="border: 1px solid #d3d3d3; padding: 15px; height: 200px;">
			<p align="center" style="margin-bottom: 0.06in">
			<font color="#000000"><font size="3" style="font-size: 12pt"><b>GIẢNG VIÊN HƯỚNG DẪN</b></font></font></p>
			<p align="center" style="margin-bottom: 0.06in">
			<font color="#000000"><font size="2" style="font-size: 11pt"><i>(Ký và ghi rõ họ tên)</i></font></font></p>
		</td>
		<td style="border: 1px solid #d3d3d3; padding: 15px; height: 200px;">
			<p align="center" style="margin-bottom: 0.06in">
			<font color="#000000"><font size="3" style="font-size: 12pt"><b>GIẢNG VIÊN PHẢN BIỆN</b></font></font></p>
			<p align="center" style="margin-bottom: 0.06in">
			<font color="#000000"><font size="2" style="font-size: 11pt"><i>(Ký và ghi rõ họ tên)</i></font></font></p>
		</td>
	</tr>
</table>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in"><font color="#000000"><font size="3" style="font-size: 12pt"><b>CHỦ
TỊCH HỘI ĐỒNG</b></font></font></p>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in"><font color="#000000"><font size="2" style="font-size: 11pt"><i>(Ký
và ghi rõ họ tên)</i></font></font></p>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in; page-break-before: always">
<font color="#000000"><font size="4" style="font-size: 14pt"><b>LỜI
CẢM ƠN</b></font></font></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để hoàn thành tiểu luận tốt nghiệp này, em xin gửi lời cảm ơn chân thành và sâu sắc nhất đến Quý Thầy Cô Khoa Công nghệ Thông tin - Trường Đại học Tân Tạo, những người đã truyền đạt cho em lượng kiến thức quý báu và định hướng nghề nghiệp vững chắc trong suốt những năm tháng học tập tại trường.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Đặc biệt, em xin gửi lời tri ân sâu sắc đến <b>Thầy Trần Ngọc Anh</b> - người Thầy đã trực tiếp tận tình hướng dẫn, chỉ bảo và sát cánh cùng em từ những bước lên ý tưởng sơ khai cho đến khi hoàn thiện toàn bộ mã nguồn và tài liệu của tiểu luận này. Sự định hướng khoa học và những lời động viên của Thầy là động lực to lớn giúp em vượt qua những khó khăn trong quá trình nghiên cứu và xây dựng hệ thống phát hiện tin giả tiếng Việt bằng học máy.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Em cũng xin gửi lời cảm ơn đến gia đình và những người bạn đã luôn ở bên cạnh động viên, khích lệ tinh thần và tạo mọi điều kiện thuận lợi nhất để em có thể toàn tâm toàn ý hoàn thành đồ án này đúng tiến độ.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mặc dù đã nỗ lực hết mình, nhưng do giới hạn về mặt thời gian và kinh nghiệm thực tiễn, tiểu luận chắc chắn không thể tránh khỏi những thiếu sót nhất định. Em rất mong nhận được những lời góp ý, chỉ bảo quý báu từ Hội đồng bảo vệ và các Thầy Cô để đề tài được hoàn thiện hơn nữa và có thể ứng dụng rộng rãi vào thực tế, góp phần xây dựng một không gian mạng Việt Nam sạch và an toàn hơn.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Cuối cùng, em xin kính chúc Quý Thầy Cô luôn dồi dào sức khỏe, hạnh phúc và gặt hái được nhiều thành công hơn nữa trong sự nghiệp trồng người cao quý.</p>

<p align="right" style="line-height: 150%; margin-top: 0.3in; margin-right: 0.5in; margin-bottom: 0.06in"><i>Tây Ninh, ngày ..... tháng ..... năm 20.....</i><br><b>Sinh viên thực hiện</b></p>

<p align="center" style="line-height: 100%; margin-bottom: 0.06in; page-break-before: always">
<font color="#000000"><font size="4" style="font-size: 14pt"><b>TÓM
TẮT TIỂU LUẬN</b></font></font></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Bộ dữ liệu được sử dụng trong nghiên cứu gồm <b>10.617 bản ghi</b> (tệp <code>full_dataset.csv</code>), sau lọc còn <b>10.609 mẫu</b> phục vụ huấn luyện. Tỷ lệ phân bố giữa hai lớp được kiểm soát chặt chẽ, góp phần loại bỏ hiện tượng mất cân bằng dữ liệu (Class Imbalance) trong quá trình huấn luyện mô hình. Điều này kết hợp với phương pháp kiểm định chéo 5-fold (Cross-validation) tạo điều kiện thuận lợi cho việc đánh giá hiệu năng mô hình một cách khách quan và đáng tin cậy.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Đối với bài toán xử lý ngôn ngữ tự nhiên tiếng Việt, mô hình PhoBERT được lựa chọn làm thành phần trích xuất đặc trưng ngữ nghĩa nhờ được tiền huấn luyện trên lượng lớn dữ liệu tiếng Việt. Việc sử dụng PhoBERT giúp mô hình khai thác hiệu quả các mối quan hệ ngữ cảnh giữa các từ và cụm từ trong văn bản, từ đó hỗ trợ nâng cao chất lượng biểu diễn dữ liệu đầu vào cho tác vụ phát hiện tin giả.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Bên cạnh mô hình dự đoán, nghiên cứu thiết kế một Động cơ giải thích rule-based độc lập (ExplanationEngine) dựa trên các đặc trưng kinh nghiệm (Heuristics). Thay vì "nhồi nhét" Heuristics vào quá trình dự đoán toán học, hệ thống chỉ chạy module này sau khi PhoBERT đã tính toán xong xác suất, nhằm sinh ra các câu văn tiếng Việt minh bạch hóa lý do bài báo bị cảnh báo (ví dụ: lạm dụng viết hoa, văn phong giật gân).</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Kết quả thực nghiệm trên tập kiểm thử (30% dữ liệu) cho thấy kiến trúc PhoBERT Text-only + MLP đạt hiệu năng cực kỳ ấn tượng: Accuracy đạt 94,13%, F1-Score 93,71%, và ROC-AUC lên tới 98,50%. Bên cạnh đó, kết quả kiểm định chéo 5-Fold (F1: 93,17% ± 1,33%) đã khẳng định tính ổn định vững chắc của mô hình. Đồng thời, việc "nhấc" cơ chế Heuristics ra ngoài trở thành Động cơ giải thích độc lập đã giải quyết triệt để tính chất "hộp đen", cung cấp lý do trực quan bằng tiếng Việt cho quyết định phân loại.</p>

<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000"><b>Từ khóa: </b> Phát hiện tin giả tiếng Việt, PhoBERT, Giải thích Heuristic, Học máy, Xử lý ngôn ngữ tự nhiên.</font></p>

<p align="center" style="line-height: 100%; margin-bottom: 0.06in; page-break-before: always; margin-top: 2in;">
<font color="#000000"><font size="4" style="font-size: 14pt"><b>ABSTRACT</b></font></font></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">The dataset utilized in this study comprises <b>10,617 labeled records</b> (<code>full_dataset.csv</code>), reduced to <b>10,609 samples</b> after cleaning for training. The distribution between the two classes is strictly controlled, contributing to the elimination of Class Imbalance during the model training phase. This establishes a favorable condition for an objective and reliable evaluation of the model's performance through 5-fold cross-validation.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">For the Vietnamese Natural Language Processing task, the PhoBERT model was selected as the semantic feature extraction component due to its extensive pre-training on a large-scale Vietnamese corpus. The employment of PhoBERT enables the model to effectively exploit the contextual relationships between words and phrases, thereby enhancing the quality of input data representation for the fake news detection task.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Alongside the predictive model, the research designs an independent rule-based Explanation Engine utilizing heuristic features. Rather than embedding heuristics into the mathematical prediction process, the system executes this module after PhoBERT has calculated the probabilities. This decoupled approach generates clear, transparent textual reasons (e.g., excessive capitalization, sensationalist tone) to justify the warnings.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Experimental results demonstrate that the proposed PhoBERT Text-only + MLP architecture achieves excellent performance (93.71% F1-Score) on the research dataset. Furthermore, decoupling the heuristics into an independent Explanation Engine effectively resolves the "black-box" nature of deep learning, providing users with intuitive, text-based reasoning for the system's classification decisions.</p>

<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000"><b>Keywords: </b> Fake News Detection, PhoBERT, Heuristic Explanation, Rule-based Engine, Text-only MLP, NLP.</font></p>
<p style="line-height: 100%; margin-bottom: 0in"><br/>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in; page-break-before: always">
<font color="#000000"><font size="4" style="font-size: 14pt"><b>MỤC
LỤC</b></font></font></p>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0in; line-height: 150%;">
    <span style="font-weight: bold;"><a href="#" style="color: black; text-decoration: none;">CHƯƠNG 1: GIỚI THIỆU</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>11</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.1. Đặt vấn đề</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>11</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.2. Mục tiêu nghiên cứu</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>11</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.2.1. Mục tiêu tổng quát</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>11</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.2.2. Mục tiêu cụ thể</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>11</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.3. Đối tượng và phạm vi nghiên cứu</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>12</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.3.1. Đối tượng nghiên cứu</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>12</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.3.2. Phạm vi nghiên cứu</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>12</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.4. Phương pháp nghiên cứu</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>12</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.5. Ý nghĩa khoa học và thực tiễn</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>12</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">1.6. Bố cục tiểu luận</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>12</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0in; line-height: 150%;">
    <span style="font-weight: bold;"><a href="#" style="color: black; text-decoration: none;">CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN NGHIÊN CỨU</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>13</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.1. Các khái niệm nền tảng</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>13</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.1.1. Tin giả (Fake News) [3, 4] và Thông tin sai lệch</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>13</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.1.2. Xử lý Ngôn ngữ Tự nhiên (Natural Language Processing - NLP)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>13</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.1.3. Trí tuệ Nhân tạo (AI) và Học máy (Machine Learning)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>13</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.1.4. Học sâu (Deep Learning) và Mạng nơ-ron (Neural Networks)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>14</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.1.5. Cơ chế Giải thích dựa trên Đặc trưng (Heuristic Explanation) [5, 8]</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>14</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.1.6. Các chỉ số đánh giá hiệu năng mô hình (Evaluation Metrics)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>14</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.2. Cơ sở lý thuyết chuyên sâu</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>15</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.2.1. Kiến trúc Transformer và Cơ chế Tự chú ý (Self-Attention)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>15</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.2.2. Mô hình PhoBERT: Cấu trúc và phương pháp tiền huấn luyện</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>16</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.2.3. Cơ sở lý thuyết của Đặc trưng kinh nghiệm (Heuristics)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>16</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.2.4. Mạng Nơ-ron Truyền thẳng (Multi-Layer Perceptron - MLP)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>16</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.2.5. Cơ sở lý thuyết về Cơ chế Giải thích dựa trên Đặc trưng (Feature-based Explanation)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>17</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.3. Tổng quan các công trình nghiên cứu liên quan</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>17</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.3.1. Các nghiên cứu trong nước</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>17</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.3.2. Các nghiên cứu ngoài nước</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>18</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.3.3. So sánh tính ưu việt của đồ án (ShieldAI) so với các hệ thống hiện tại</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>18</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.4. Công nghệ và Công cụ sử dụng</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>20</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.4.3. Thư viện Trí tuệ Nhân tạo và Xử lý Ngôn ngữ</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>20</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.5. Biện luận lựa chọn kiến trúc AI</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>20</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.5.1. Lựa chọn Mô hình Ngôn ngữ Lõi (PhoBERT)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>20</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.5.2. Lựa chọn Kiến trúc PhoBERT Text-only + MLP</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>21</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.5.3. Lựa chọn cơ chế giải thích dựa trên đặc trưng</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>21</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">2.6. Kết luận chương</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>21</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.1. Phương pháp nghiên cứu</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>23</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.1.1. Phân tích Dữ liệu nghiên cứu (Dataset Analysis)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>23</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.1.2. Tiền xử lý và Làm sạch Dữ liệu (Data Cleaning)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>23</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.1.3. Phân chia Dữ liệu Huấn luyện (Data Split)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>24</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.1.4. Phương pháp Trích xuất đặc trưng đa chiều (Multi-dimensional Feature Extraction)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>24</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.1.5. Phương pháp Mô hình hóa mạng đa tầng (PhoBERT Text-only + MLP)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>24</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.1.6. Phương pháp Đánh giá và Giải thích (Explainability Integration)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>25</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.2. Công nghệ triển khai hệ thống phần mềm</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>25</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.3. Phân tích yêu cầu</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>26</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.3.1. Yêu cầu chức năng</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>26</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.3.2. Yêu cầu phi chức năng</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>27</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.4. Thiết kế hệ thống</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>28</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.4.1. Kiến trúc hệ thống</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>28</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.4.2. Thiết kế cơ sở dữ liệu và Mô hình Thực thể - Mối quan hệ (ERD)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>31</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.4.3. Thiết kế giao diện (UI/UX Design) và Trải nghiệm Người dùng</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>35</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.4.4. Thiết kế thuật toán (Thuật toán PhoBERT + MLP - PhoBERT + MLP)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>36</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">3.5. Kết luận chương</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>42</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.1. Môi trường phát triển và Thực nghiệm</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>43</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.1.1. Môi trường Phần cứng (Hardware Environment)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>43</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.1.2. Môi trường Hệ điều hành và Phần mềm</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>43</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.2. Quá trình hiện thực</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>44</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.2.1. Cài đặt các module lõi của hệ thống (Core Modules Implementation)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>44</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.2.2. Dữ liệu nghiên cứu và Quy trình Tiền xử lý</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>45</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.2.3. Tổ chức cấu trúc mã nguồn (Project Directory Structure)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>47</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.3. Kết quả đạt được</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>48</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.3.1. Kết quả giao diện ứng dụng (User Interface Implementation)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>48</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.3.2. Đánh giá kết quả bằng số liệu thực nghiệm</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>51</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.4. Kiểm thử hệ thống (System Testing)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>53</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.4.1. Kiểm thử tự động bằng Pytest (Automated Testing)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>53</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.6in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.4.1.1. Phân nhóm và chi tiết 42 test cases (Bảng 4.4)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>54</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.4in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.4.2. Kiểm thử Hộp đen mức Ứng dụng (Manual Black-box Testing)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>54</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">4.5. Kết luận chương</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>57</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">5.1. Kết luận</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>58</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">5.2. Đóng góp của tiểu luận (Tính mới &amp; Tính Sáng tạo)</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>58</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">5.3. Hạn chế của đề tài</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>59</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">5.4. Hướng phát triển</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>60</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0in; line-height: 150%;">
    <span style="font-weight: bold;"><a href="#" style="color: black; text-decoration: none;">TÀI LIỆU THAM KHẢO</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>62</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0in; line-height: 150%;">
    <span style="font-weight: bold;"><a href="#" style="color: black; text-decoration: none;">PHỤ LỤC</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>64</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">Phụ lục A: Mã nguồn chương trình</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>64</span>
</div>
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.07in; margin-left: 0.2in; line-height: 150%;">
    <span style="font-weight: normal;"><a href="#" style="color: black; text-decoration: none;">Phụ lục B: Hướng dẫn sử dụng</a></span>
    <span style="flex-grow: 1; border-bottom: 2px dotted #000; margin: 0 10px; position: relative; top: -4px;"></span>
    <span>65</span>
</div>

<p align="center" style="line-height: 100%; margin-bottom: 0.06in; page-break-before: always">
<font color="#000000"><font size="4" style="font-size: 14pt"><b>DANH
MỤC HÌNH ẢNH</b></font></font></p>

<table width="100%" border="1" cellpadding="8" cellspacing="0" style="display: table; width: 100%; border-collapse: collapse; border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; table-layout: fixed; word-wrap: break-word; word-break: break-word; white-space: normal;">
  <tr style="background-color: #f2f2f2;">
    <th width="15%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Số hiệu</th>
    <th width="70%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Tên hình ảnh</th>
    <th width="15%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center;">Trang</th>
  </tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.1</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Giao diện màn hình Cổng thông tin (Home) với thiết kế tối giản, tông màu tối chuyên nghiệp</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">30</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.2</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Giao diện Đăng nhập (Authentication) bảo mật người dùng</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">31</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.3</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Giao diện trung tâm Phân tích — nhập văn bản thô hoặc URL để kiểm chứng</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">32</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.4</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Báo cáo phân tích cảnh báo nguy cơ Tin Giả thông qua nguyên lý Thị giác hóa rủi ro (Màu Đỏ)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">33</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.5</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Báo cáo phân tích xác thực Tin Thật an toàn (Màu Xanh lá cây)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">34</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.6</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Trình diễn khả năng của Động cơ Giải thích: Hệ thống bóc tách rõ lý do bài báo bị đánh dấu lừa đảo</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">35</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.7</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Màn hình Quản lý Lịch sử cá nhân với thiết kế dạng danh sách thẻ động (Dynamic Cards)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">36</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.8</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Minh họa Kịch bản TC_01: Phân tích bài báo chính thống (0% Tin giả)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">40</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.11</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Minh họa Kịch bản TC_02: Ngăn chặn lỗi khi phân tích URL sai định dạng</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">41</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hình 4.12</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Minh họa Kịch bản TC_03: Bóc trần thủ thuật lạm dụng hình thức (100% Tin giả)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">42</td></tr>
</table>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in"><font color="#000000"><font size="4" style="font-size: 14pt"><b>DANH
MỤC BẢNG BIỂU</b></font></font></p>
<table width="100%" border="1" cellpadding="8" cellspacing="0" style="display: table; width: 100%; border-collapse: collapse; border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; table-layout: fixed; word-wrap: break-word; word-break: break-word; white-space: normal;">
  <tr style="background-color: #f2f2f2;">
    <th width="15%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Số hiệu</th>
    <th width="70%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Tên bảng biểu</th>
    <th width="15%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center;">Trang</th>
  </tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Bảng 3.1</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Yêu cầu chức năng hệ thống (FR-01 … FR-08)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">23</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Bảng 3.2</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Từ điển Dữ liệu (Data Dictionary) cho các Thực thể</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">25</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Bảng 4.1</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hiệu năng của mô hình PhoBERT Text-only + MLP</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">38</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Bảng 4.2</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Danh sách Kịch bản Kiểm thử Hộp đen</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">39</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Bảng 4.3</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Bộ kiểm thử tự động Pytest — tổng quan theo file</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">40</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Bảng 4.4</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Chi tiết từng kịch bản kiểm thử tự động (42 test cases)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center; font-weight: bold;">41</td></tr>
</table>
<p align="center" style="line-height: 100%; margin-bottom: 0.06in"><font color="#000000"><font size="4" style="font-size: 14pt"><b>DANH
MỤC TỪ VIẾT TẮT</b></font></font></p>
<table width="100%" border="1" cellpadding="8" cellspacing="0" style="display: table; width: 100%; border-collapse: collapse; border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; table-layout: fixed; word-wrap: break-word; word-break: break-word; white-space: normal;">
  <tr style="background-color: #f2f2f2;">
    <th width="20%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Từ viết tắt</th>
    <th width="80%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Giải thích thuật ngữ tiếng Anh (tiếng Việt)</th>
  </tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>AI</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Artificial Intelligence (Trí tuệ nhân tạo)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>API</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Application Programming Interface (Giao diện lập trình ứng dụng)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>BERT</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Bidirectional Encoder Representations from Transformers (Mô hình biểu diễn ngôn ngữ hai chiều từ Transformer)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>DL</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Deep Learning (Học sâu)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>DOM</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Document Object Model (Mô hình Đối tượng Tài liệu)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ERD</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Entity-Relationship Diagram (Sơ đồ Thực thể - Mối quan hệ)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>HTML</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">HyperText Markup Language (Ngôn ngữ đánh dấu siêu văn bản)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>JSON</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">JavaScript Object Notation (Định dạng trao đổi dữ liệu)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ML</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Machine Learning (Học máy)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>MLP</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Multilayer Perceptron (Mạng nơ-ron truyền thẳng đa tầng)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>NLP</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Natural Language Processing (Xử lý Ngôn ngữ Tự nhiên)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ORM</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Object-Relational Mapping (Ánh xạ đối tượng - quan hệ)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>UI / UX</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">User Interface / User Experience (Giao diện người dùng / Trải nghiệm người dùng)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>URL</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Uniform Resource Locator (Định vị tài nguyên thống nhất)</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>Giải thích Heuristic</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Explainable Artificial Intelligence (Trí tuệ nhân tạo có thể giải thích / AI Minh bạch)</td></tr>
</table>
<h1 style="page-break-before: always">CHƯƠNG 1: GIỚI THIỆU</h1>
<h2>1.1. Đặt vấn đề</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Sự bùng nổ của mạng xã hội đã tạo điều kiện cho "tin giả" (Fake News) lan truyền, thao túng dư luận và gây rủi ro xã hội. Dù các mô hình Học sâu như Transformer và PhoBERT đã đạt nhiều tiến bộ trong việc phân tích văn bản, chúng vẫn bộc lộ hạn chế lớn là tính chất "hộp đen" và thiếu khả năng diễn giải kết quả cho người dùng cuối. Do đó, đề tài <b>"Nghiên cứu, xây dựng công cụ phân tích và phát hiện tin giả tiếng Việt bằng PhoBERT và mạng nơ-ron đa tầng (Hệ thống ShieldAI)"</b> được thực hiện nhằm giải quyết vấn đề này.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Đề tài tập trung nghiên cứu và xây dựng hệ thống phân loại tin giả dựa trên mô hình ngôn ngữ lớn PhoBERT kết hợp với mạng nơ-ron truyền thẳng (MLP). Hệ thống này tập trung khai thác các đặc trưng ngữ nghĩa từ văn bản để đưa ra phán quyết chuẩn xác. Đặc biệt, nhằm khắc phục nhược điểm "hộp đen", nghiên cứu đề xuất tích hợp một Động cơ giải thích (Explanation Engine) độc lập dựa trên luật và các đặc trưng kinh nghiệm (Heuristics) — nhằm bóc tách các dấu hiệu thao túng cảm xúc, văn phong giật gân, sự lạm dụng dấu câu — từ đó cung cấp những lý giải trực quan, minh bạch cho quyết định phân loại của mô hình.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để đánh giá tính khả thi của phương pháp đề xuất, mô hình được triển khai và kiểm thử trên bộ dữ liệu tin tức tiếng Việt đã được gán nhãn. Các chỉ số đánh giá cốt lõi như Accuracy, Precision, Recall và F1-Score được sử dụng để phân tích hiệu năng của mạng phân loại. Kết quả thực nghiệm, tính hiệu quả của cơ chế giải thích cùng các phân tích chi tiết sẽ được trình bày trong chương đánh giá của tiểu luận.</p>

<h2>1.2. Mục tiêu nghiên cứu</h2>
<h3>1.2.1. Mục tiêu tổng quát</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Phát triển nền tảng Web kiểm duyệt tin giả tiếng Việt tự động, ứng dụng kiến trúc AI tinh gọn (PhoBERT Text-only + MLP) và cơ chế giải thích dựa trên đặc trưng để minh bạch hóa quyết định, đồng thời quản lý lịch sử tra cứu của người dùng an toàn.</p>

<h3>1.2.2. Mục tiêu cụ thể</h3>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Hệ thống hóa lý thuyết:</b> Tổng hợp tri thức về NLP, mô hình PhoBERT, phân loại MLP (scikit-learn) và giải thích rule-based (XAI).</li>
  <li style="margin-bottom: 0.05in;"><b>Tối ưu mô hình PhoBERT + MLP:</b> Sử dụng vector [CLS] 768 chiều duy nhất từ PhoBERT kết hợp mạng MLP (128, 64) để tăng độ chính xác phân loại.</li>
  <li style="margin-bottom: 0.05in;"><b>Xây dựng Động cơ giải thích (Explanation Engine):</b> Thiết kế module rule-based độc lập chạy sau khi mô hình dự đoán xong, nhằm sinh ra câu văn tiếng Việt minh bạch hóa lý do bài báo bị cảnh báo.</li>
  <li style="margin-bottom: 0.05in;"><b>Phát triển nền tảng phần mềm hoàn chỉnh:</b> Thiết kế và triển khai kiến trúc Client-Server chuyên nghiệp để biến mô hình AI nghiên cứu thành sản phẩm thực tiễn (ShieldAI), mang lại trải nghiệm tương tác liền mạch cho người dùng đầu cuối.</li>
  <li style="margin-bottom: 0.05in;"><b>Đánh giá mô hình:</b> So sánh hiệu năng mô hình đề xuất với các thuật toán truyền thống (Decision Tree, Naive Bayes).</li>
</ul>

<h2>1.3. Đối tượng và phạm vi nghiên cứu</h2>
<h3>1.3.1. Đối tượng nghiên cứu</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Bao gồm: (1) Mô hình ngôn ngữ lớn PhoBERT; (2) Bộ phân loại MLP (scikit-learn); (3) Pipeline tiền xử lý <code>preprocess_text</code>; (4) Giải thích rule-based (<code>ExplanationEngine</code>); và (5) Công nghệ Web (FastAPI, Next.js, SQLite).</p>

<h3>1.3.2. Phạm vi nghiên cứu</h3>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Mục tiêu phân loại:</b> Thay vì tiếp cận theo hướng nhị phân cứng nhắc, hệ thống ShieldAI cung cấp trải nghiệm người dùng (UX) tinh tế hơn với 3 mức độ cảnh báo: Tin thật (Xác suất &lt; 35%), Đáng ngờ (35% - 74%), và Tin giả (Xác suất &ge; 75%).</li>
  <li style="margin-bottom: 0.05in;"><b>Thuật toán:</b> Tập trung vào kiến trúc PhoBERT Text-only + MLP, lấy vector [CLS] 768 chiều từ PhoBERT đưa qua mạng nơ-ron truyền thẳng đa tầng.</li>
  <li style="margin-bottom: 0.05in;"><b>Cấu trúc Triển khai ứng dụng (Deployment):</b> Đồ án được hệ thống hóa hoàn chỉnh theo kiến trúc Client-Server chuyên nghiệp. Giao diện người dùng (Frontend) được phát triển bằng Next.js 14 mang lại trải nghiệm tương tác mượt mà; Máy chủ (Backend) sử dụng FastAPI bất đồng bộ cho hiệu năng cao; Dữ liệu lịch sử quét tin giả được lưu trữ an toàn bằng SQLite. Đặc biệt, hệ thống tích hợp Trình thu thập dữ liệu (Web Crawler) bằng BeautifulSoup giúp tự động cào nội dung bài báo trực tiếp từ URL, tối ưu hóa đáng kể trải nghiệm người dùng (UX) thay vì ép người dùng dán văn bản thuần túy.</li>
</ul>

<h2>1.4. Phương pháp nghiên cứu</h2>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Đề tài sử dụng: (1) Phương pháp nghiên cứu lý thuyết; (2) Phương pháp thu thập và làm sạch dữ liệu; (3) Phương pháp thực nghiệm, mô hình hóa; và (4) Phương pháp thống kê, đánh giá định lượng.</p>

<h2>1.5. Ý nghĩa khoa học và thực tiễn</h2>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in"><b>Về khoa học:</b> Khẳng định năng lực của kiến trúc PhoBERT Text-only + MLP trên ngữ liệu tiếng Việt, đóng góp tài liệu vào lý thuyết Giải thích Heuristic và thiết lập thang đo (benchmark) tin cậy cho các nghiên cứu xử lý ngôn ngữ.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in"><b>Về thực tiễn:</b> Cung cấp cho cộng đồng công cụ phân loại tin giả trực quan, đồng thời mở ra cơ hội tích hợp vào các hệ thống kiểm duyệt tự động trên không gian mạng đa lĩnh vực.</p>

<h2>1.6. Bố cục tiểu luận</h2>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Đồ án được cấu trúc thành 5 chương: <b>Chương 1</b> giới thiệu chung; <b>Chương 2</b> trình bày cơ sở lý thuyết; <b>Chương 3</b> phân tích thiết kế hệ thống; <b>Chương 4</b> công bố kết quả thực nghiệm; <b>Chương 5</b> tổng kết và đề xuất hướng phát triển.</p>

<h1 style="page-break-before: always">CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN NGHIÊN CỨU</h1>
<h2>2.1. Các khái niệm nền tảng</h2>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Để xây dựng một kiến trúc hệ thống phân tích tin giả phức tạp, việc nắm bắt các khái niệm cốt lõi mang tính chất nền tảng là điều kiện tiên quyết. Mục này sẽ trình bày và định nghĩa một cách khoa học các thuật ngữ chuyên ngành được sử dụng xuyên suốt trong đồ án.</p>

<h3>2.1.1. Tin giả (Fake News) [3, 4] và Thông tin sai lệch</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Trong kỷ nguyên số, <b>Tin giả (Fake News) [3, 4]</b> được định nghĩa là những thông tin sai sự thật, bị bóp méo, hoặc bịa đặt hoàn toàn, được trình bày dưới hình thức tin báo chí nhằm mục đích lừa dối người đọc. Điểm khác biệt mấu chốt của tin giả so với các lỗi sai sót báo chí thông thường nằm ở <b>động cơ (intent)</b>. Tin giả được tạo ra một cách có chủ đích nhằm thu lợi ích tài chính (thông qua việc thu hút lượt nhấp chuột - clickbait để lấy doanh thu quảng cáo) hoặc phục vụ các mục đích chính trị, thao túng tâm lý và định hướng dư luận xã hội.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Hội đồng Châu Âu (Council of Europe) phân loại thông tin sai lệch thành ba nhóm chính: <i>Mis-information</i> (Thông tin sai nhưng không có ác ý), <i>Dis-information</i> (Thông tin sai và có ác ý, bịa đặt), và <i>Mal-information</i> (Thông tin có thật nhưng được dùng để bôi nhọ, hãm hại người khác). Đồ án này tập trung chủ yếu vào việc tự động nhận diện và phát hiện nhóm Dis-information, đặc biệt là các bài viết sử dụng ngôn từ kích động và cấu trúc câu lừa đảo trên mạng xã hội tiếng Việt.</p>

<h3>2.1.2. Xử lý Ngôn ngữ Tự nhiên (Natural Language Processing - NLP)</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in"><b>Xử lý Ngôn ngữ Tự nhiên (NLP)</b> là một phân ngành giao thoa giữa Khoa học Máy tính, Trí tuệ Nhân tạo và Ngôn ngữ học. Mục tiêu của NLP là thu hẹp khoảng cách giao tiếp giữa con người và máy tính bằng cách cung cấp cho máy tính khả năng đọc, hiểu, phân tích và trích xuất ý nghĩa từ ngôn ngữ tự nhiên của con người.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Trong khuôn khổ bài toán phát hiện tin giả, NLP đóng vai trò xương sống. Văn bản thô ban đầu là một dạng dữ liệu phi cấu trúc (unstructured data) mà máy tính không thể tính toán trực tiếp. Thông qua các kỹ thuật NLP như làm sạch văn bản (text cleaning), tách từ (tokenization), và biểu diễn từ ngữ dưới dạng không gian vector toán học (word embeddings), NLP biến đổi ngôn ngữ loài người thành các ma trận số liệu có cấu trúc để đưa vào huấn luyện mạng nơ-ron.</p>

<h3>2.1.3. Trí tuệ Nhân tạo (AI) và Học máy (Machine Learning)</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in"><b>Trí tuệ Nhân tạo (AI)</b> là thuật ngữ rộng chỉ khả năng của máy móc mô phỏng các chức năng nhận thức của con người như học tập và giải quyết vấn đề. Nằm bên trong lõi của AI hiện đại là <b>Học máy (Machine Learning - ML)</b>. Thay vì được lập trình bằng các quy tắc logic &quot;If-Else&quot; cứng nhắc do lập trình viên định sẵn, Học máy cho phép các thuật toán tự động nhận diện các mẫu (patterns) ẩn sâu trong một khối lượng dữ liệu khổng lồ, từ đó tự đúc kết quy luật để đưa ra dự đoán cho các dữ liệu mới trong tương lai.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Bài toán phát hiện tin giả trong đồ án thuộc phân lớp bài toán <b>Học có giám sát (Supervised Learning)</b>. Về cơ bản, hệ thống được cung cấp hàng chục ngàn bài báo đã được con người dán nhãn trước để huấn luyện thuật toán. Tuy nhiên, thay vì áp dụng một ranh giới quyết định (decision boundary) nhị phân cứng nhắc (Thật/Giả) ở bước dự đoán cuối cùng, hệ thống chia xác suất thành 3 mức độ cảnh báo (Verdict) linh hoạt để tăng tính thân thiện và chính xác trong trải nghiệm người dùng (UX).</p>

<h3>2.1.4. Học sâu (Deep Learning) và Mạng nơ-ron (Neural Networks)</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in"><b>Học sâu (Deep Learning)</b> là một tập con tiên tiến nhất của Học máy, lấy cảm hứng từ cấu trúc phân tầng và hoạt động của bộ não sinh học. Các hệ thống học sâu sử dụng <b>Mạng nơ-ron nhân tạo (Artificial Neural Networks)</b> với hàng chục đến hàng trăm lớp ẩn (hidden layers) được xếp chồng lên nhau. Khả năng vượt trội của Học sâu nằm ở chỗ nó có thể tự động trích xuất các biểu diễn đặc trưng (feature representation) ở mức độ trừu tượng rất cao từ dữ liệu thô mà không cần hoặc cần rất ít sự can thiệp kỹ thuật thủ công từ con người (feature engineering).</p>

<h3>2.1.5. Cơ chế Giải thích dựa trên Đặc trưng (Heuristic Explanation) [5, 8]</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Mặc dù Mạng nơ-ron Học sâu mang lại độ chính xác cực kỳ ấn tượng, chúng lại mắc phải điểm yếu chí mạng là tính chất <b>&quot;Hộp đen&quot; (Black-box)</b>. Nghĩa là, kỹ sư có thể nạp dữ liệu vào và nhận kết quả đầu ra rất chuẩn xác, nhưng không ai có thể truy xuất ngược quá trình tính toán hàng triệu tham số bên trong để hiểu tại sao mô hình lại đi đến quyết định đó.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Để giải quyết vấn đề niềm tin và tính đạo đức này, khái niệm <b>Cơ chế Giải thích dựa trên Đặc trưng (Heuristic Explanation) [5, 8]</b> ra đời. Giải thích Heuristic tập hợp các thuật toán nhằm minh bạch hóa kết quả đầu ra của Học sâu, giúp con người có thể lý giải một cách trực quan. Trong hệ thống phát hiện tin giả, Giải thích Heuristic là cơ sở lý thuyết để xây dựng nên Động cơ giải thích, giúp máy tính trả lời được câu hỏi mang tính phản biện: <i>&quot;Những đặc trưng hoặc từ vựng cụ thể nào đã khiến văn bản này bị phân loại là giả mạo?&quot;</i>.</p>

<h3>2.1.6. Các chỉ số đánh giá hiệu năng mô hình (Evaluation Metrics)</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Để đo lường một cách khách quan năng lực phân loại của hệ thống, đồ án sử dụng các thang đo chuẩn quốc tế dựa trên <b>Ma trận nhầm lẫn (Confusion Matrix)</b>. Ma trận này phân tách kết quả thành 4 nhóm: <i>True Positive - TP</i> (Hệ thống bắt đúng tin giả), <i>True Negative - TN</i> (Hệ thống nhận diện đúng tin thật), <i>False Positive - FP</i> (Hệ thống nhận diện nhầm tin thật thành tin giả), và <i>False Negative - FN</i> (Hệ thống bỏ sót tin giả). Từ ma trận này, đồ án sử dụng 4 chỉ số cốt lõi:</p>

<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Độ chính xác tổng thể (Accuracy):</b> Là tỷ lệ phần trăm số bài báo (cả thật và giả) được hệ thống phân loại đúng trên tổng số các bài báo trong tập kiểm thử. Tuy nhiên, trong môi trường thực tế (nơi lượng tin thật thường áp đảo tin giả), Accuracy không phải là thước đo duy nhất đáng tin cậy.</li>
  <li style="margin-bottom: 0.05in;"><b>Độ chuẩn xác (Precision):</b> Trả lời cho câu hỏi: <i>&quot;Trong số những bài báo mà hệ thống dán nhãn là tin giả, có bao nhiêu phần trăm thực sự là tin giả?&quot;</i>. Chỉ số này đặc biệt quan trọng để hệ thống giảm thiểu tối đa <i>False Positive</i> (ngăn chặn việc vu khống hoặc kiểm duyệt nhầm các bài báo chân chính).</li>
  <li style="margin-bottom: 0.05in;"><b>Độ bao phủ (Recall / Sensitivity):</b> Trả lời cho câu hỏi: <i>&quot;Trong tổng số toàn bộ tin giả đang tồn tại thực tế, hệ thống đã bắt thành công bao nhiêu phần trăm?&quot;</i>. Recall cao đồng nghĩa với việc hệ thống có khả năng càn quét tốt, giảm thiểu <i>False Negative</i> (không để lọt lưới tin độc hại).</li>
  <li style="margin-bottom: 0.05in;"><b>Điểm F1 (F1-Score):</b> Là trung bình điều hòa (Harmonic Mean) giữa Precision và Recall. Đây là chỉ số tối thượng (Ultimate Metric) được đồ án sử dụng làm tiêu chuẩn chính để quyết định mô hình nào hoạt động tốt nhất. F1-Score đảm bảo sự cân bằng hiệu quả, buộc hệ thống vừa không được phép &quot;bắt nhầm&quot; (Precision cao) vừa không được &quot;bỏ sót&quot; (Recall cao).</li>
</ul>

<h2>2.2. Cơ sở lý thuyết chuyên sâu</h2>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Nếu mục 2.1 dừng lại ở việc định nghĩa các khái niệm nền tảng, thì mục này sẽ đi sâu vào việc mổ xẻ cấu trúc toán học và logic vận hành bên trong của các thành phần cốt lõi cấu thành nên hệ thống AI (PhoBERT Text-only + MLP).</p>

<h3>2.2.1. Kiến trúc Transformer và Cơ chế Tự chú ý (Self-Attention)</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Trước khi kiến trúc Transformer [6, 7] ra đời (được giới thiệu bởi Vaswani et al., 2017), các bài toán NLP chủ yếu dựa vào mạng nơ-ron hồi quy (RNN) hoặc bộ nhớ ngắn hạn dài (LSTM). Hạn chế lớn nhất của RNN/LSTM là tính toán tuần tự, dẫn đến hiện tượng &quot;quên&quot; ngữ cảnh đối với các câu văn dài và không thể tính toán song song. Transformer ra đời đã phá vỡ hoàn toàn rào cản này bằng cách loại bỏ hoàn toàn cấu trúc hồi quy, thay vào đó sử dụng độc quyền cơ chế <b>Tự chú ý (Self-Attention)</b>.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Cơ sở toán học của Self-Attention xoay quanh ba ma trận: <i>Query (Q), Key (K)</i>, và <i>Value (V)</i>. Với mỗi từ trong câu, mô hình sẽ tính toán điểm số chú ý (Attention Score) của từ đó so với tất cả các từ khác trong cùng một ngữ cảnh thông qua việc nhân ma trận (Dot-product) và áp dụng hàm Softmax. Điểm số này giúp mô hình hiểu được tầm quan trọng và sự phụ thuộc về mặt ngữ pháp/ngữ nghĩa lẫn nhau giữa các từ, bất kể khoảng cách vật lý của chúng trong câu là bao xa. Cấu trúc này cho phép máy tính xử lý song song toàn bộ văn bản, tạo ra những ma trận biểu diễn (embeddings) cực kỳ sắc bén.</p>

<h3>2.2.2. Mô hình PhoBERT: Cấu trúc và phương pháp tiền huấn luyện</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in"><b>PhoBERT</b> là một mô hình ngôn ngữ lớn (LLM) tiên phong được huấn luyện dành riêng cho tiếng Việt. Về mặt kiến trúc cốt lõi, PhoBERT không kế thừa nguyên bản BERT của Google, mà dựa trên biến thể được tối ưu hóa mạnh mẽ hơn là <b>RoBERTa (Robustly Optimized BERT Pretraining Approach)</b>.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Khác biệt chuyên sâu của PhoBERT nằm ở chiến lược huấn luyện. Trong khi BERT sử dụng kỹ thuật <i>Masked Language Model (MLM)</i> tĩnh (các từ bị che giấu cố định trong suốt quá trình huấn luyện), PhoBERT áp dụng <b>MLM động (Dynamic Masking)</b>. Nghĩa là, ở mỗi chu kỳ huấn luyện (epoch), các từ bị che khuất sẽ thay đổi liên tục một cách ngẫu nhiên. Điều này buộc mạng nơ-ron phải học cách dự đoán từ còn thiếu dựa trên các cấp độ từ vựng ghép của tiếng Việt. Được tiền huấn luyện trên khối dữ liệu 20GB, PhoBERT sở hữu khả năng nắm bắt cấu trúc ngữ pháp, từ ghép và ngữ cảnh phức tạp của tiếng Việt với hiệu năng vượt trội.</p>

<h3>2.2.3. Cơ sở lý thuyết của Đặc trưng kinh nghiệm (Heuristics)</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Trong bài toán phân loại thông tin độc hại, nếu PhoBERT đảm nhiệm phần "Ngữ nghĩa học" (Semantics) để phân loại, thì các đặc trưng Heuristics đảm nhiệm phần "Hành vi học" (Behavioral Analysis) để giải thích kết quả. Cơ sở lý thuyết của việc sử dụng Heuristics độc lập này bắt nguồn từ việc tin giả thường có cấu trúc <i>thiết kế có chủ ý</i> để thao túng cảm xúc người đọc, và việc chỉ ra các thủ thuật này giúp người dùng dễ hiểu lý do cảnh báo hơn.</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Phân tích Cảm xúc (Sentiment Analysis):</b> Các bài báo mạo danh thường lạm dụng các từ ngữ mang sắc thái cảm xúc cực đoan (kích động thù hằn, tạo sự hoang mang, sợ hãi) để ép buộc người đọc phải chia sẻ (share) ngay lập tức. Việc định lượng điểm số tiêu cực/tích cực (Polarity Score) đóng vai trò như một mỏ neo nhận diện.</li>
  <li style="margin-bottom: 0.05in;"><b>Kỹ thuật Clickbait:</b> Tin giả thường sử dụng thủ thuật viết hoa toàn bộ tựa đề (CAPS LOCK) hoặc lạm dụng dấu câu (ví dụ: !!!, ???) để gây chú ý trực quan mạnh. Hệ thống sử dụng Biểu thức chính quy (Regular Expression) để trích xuất và đo lường mật độ của các dấu hiệu bất thường này.</li>
</ul>

<h3>2.2.4. Mạng Nơ-ron Truyền thẳng (Multi-Layer Perceptron - MLP)</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Hệ thống sử dụng kiến trúc <b>Mạng nơ-ron truyền thẳng (Multi-Layer Perceptron - MLP)</b> để làm bộ phân loại lõi. Lớp MLP này nhận đầu vào là vector nhúng ngữ nghĩa duy nhất gồm 768 chiều được trích xuất từ token [CLS] của mô hình PhoBERT. Vector này được chuẩn hóa (StandardScaler) trước khi đưa vào các lớp ẩn.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Cấu trúc MLP sử dụng <code>sklearn.neural_network.MLPClassifier</code> với lớp ẩn <b>(128, 64)</b>, hàm kích hoạt ReLU, solver Adam, <code>alpha=0.1</code> (chuẩn hóa L2) và <code>early_stopping=True</code> để chống overfitting. <code>predict_proba</code> trả xác suất tin giả; module <code>verdict.py</code> quy đổi thành 3 mức cảnh báo: Tin thật (&lt;35%), Đáng ngờ (35–74%), Tin giả (≥75%).</p>

<h3>2.2.5. Cơ sở lý thuyết về Cơ chế Giải thích dựa trên Đặc trưng (Feature-based Explanation)</h3>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Bên cạnh việc đưa ra kết quả phân loại, hệ thống còn được thiết kế một Động cơ giải thích rule-based độc lập (ExplanationEngine) nhằm cung cấp các thông tin hỗ trợ người dùng hiểu rõ hơn lý do của dự đoán. Thay vì sử dụng các kỹ thuật Giải thích Trí tuệ nhân tạo (Explainable AI - XAI) phức tạp như SHAP hay LIME để mổ xẻ nội bộ mạng nơ-ron, nghiên cứu áp dụng phương pháp giải thích bằng luật dựa trên các đặc trưng kinh nghiệm (Heuristics) chạy độc lập sau bước phân loại.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Cơ chế này hoạt động bằng cách quét qua bài báo để phân tích các đặc trưng hình thức như tỷ lệ chữ in hoa, số lượng dấu chấm than, độ dài tiêu đề. Khi một đặc trưng vượt quá ngưỡng đã được lập trình sẵn, hệ thống sẽ tự động sinh ra các câu văn tiếng Việt (ví dụ: "Tiêu đề bài báo lạm dụng viết hoa") để trình bày trực tiếp cho người dùng.</p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Phương pháp này hoàn toàn tách biệt khỏi cấu trúc mạng nơ-ron lõi, không làm ảnh hưởng đến thời gian dự đoán của PhoBERT, mà vẫn giải quyết trọn vẹn tính chất "hộp đen". Nhờ đó, người dùng cuối nhận được những lý giải trực quan, minh bạch và dễ hiểu bằng ngôn ngữ tự nhiên thay vì những biểu đồ XAI phức tạp.</p>
<h2>2.3. Tổng quan các công trình nghiên cứu liên quan</h2>
<h3>2.3.1. Các nghiên cứu trong nước</h3>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><i>ReINTEL Challenge 2020: Vietnamese Fake News Detection using Ensemble Model with PhoBERT embeddings</i> (Nhiều tác giả, Hội thảo VLSP 2020): Nghiên cứu này đã ứng dụng thành công mô hình ngôn ngữ PhoBERT để trích xuất đặc trưng văn bản, kết hợp với các thuật toán Ensemble (StackNet, LightGBM) để đạt F1-Score lên tới 94% trên tập dữ liệu ReINTEL, khẳng định khả năng của PhoBERT trong bài toán tiếng Việt.</li>
  <li style="margin-bottom: 0.05in;"><i>Phát hiện tự động tin giả: Thành tựu và thách thức</i> (Tạp chí Khoa học và Công nghệ - Đại học Đà Nẵng, 2021): Công trình đã hệ thống hóa và so sánh hiệu năng của hàng loạt phương pháp học máy (BoW, TF-IDF, SVM) và học sâu (CNN, LSTM) trên ngữ liệu tiếng Việt, chỉ ra giới hạn về bộ nhớ ngữ cảnh của các mạng nơ-ron thế hệ cũ khi xử lý văn bản dài.</li>
  <li style="margin-bottom: 0.05in;"><i>Fake News Detection using PhoBERT and BiLSTM with Handcrafted Features</i> (Nhóm nghiên cứu thuộc các trường Đại học tại Việt Nam, 2022): Nghiên cứu đã đề xuất PhoBERT + MLP ghép thành công giữa mô hình PhoBERT [1] và mạng hồi quy BiLSTM, đồng thời chứng minh việc bổ sung các đặc trưng đếm thủ công (độ dài văn bản, thời gian đăng) giúp cải thiện đáng kể khả năng nhận diện tin giả so với việc chỉ dùng văn bản thô.</li>
  <li style="margin-bottom: 0.05in;"><i>Nhận diện thông tin sai lệch đa phương thức trên mạng xã hội tiếng Việt</i> (Các nghiên cứu tham gia VLSP ReINTEL): Các nghiên cứu tiên phong đã xây dựng thành công mô hình trích xuất đặc trưng song song từ cả văn bản (PhoBERT) và hình ảnh đính kèm (CNN/Swin Transformer), mở ra hướng đi mới trong việc phát hiện tin giả dạng ảnh chế (meme) trên Facebook.</li>
</ul>

<h3>2.3.2. Các nghiên cứu ngoài nước</h3>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><i>Fake News Detection on Social Media: A Data Mining Perspective</i> (Kai Shu et al., 2017): Nghiên cứu đã định nghĩa và phân tách thành công bộ đặc trưng phát hiện tin giả thành hai nhóm lõi: Đặc trưng nội dung (văn phong giật gân, độ dài) và Đặc trưng mạng xã hội (tương tác người dùng). Đây là công trình đặt nền móng cho việc sử dụng Heuristics trong phân tích tin giả.</li>
  <li style="margin-bottom: 0.05in;"><i>Emotion shapes the diffusion of moralized content in social networks</i> (William J. Brady et al., Tạp chí PNAS, 2017): Nhóm tác giả đã chứng minh bằng thực nghiệm thống kê rằng các bài đăng chứa từ vựng mang cảm xúc phẫn nộ và sợ hãi có tốc độ lan truyền nhanh hơn tin thật gấp nhiều lần. Kết quả này xác thực tầm quan trọng của tính năng Phân tích cảm xúc (Sentiment Analysis).</li>
  <li style="margin-bottom: 0.05in;"><i>dEFEND: Explainable Fake News Detection</i> (Kai Shu et al., Hội nghị KDD 2019): Nghiên cứu đã xây dựng thành công một mô hình không chỉ phân loại tin giả mà còn sử dụng cơ chế Attention để tự động bôi đậm (highlight) các câu văn lừa đảo. Đây là một trong những công trình đầu tiên hiện thực hóa khái niệm Heuristic Explanation trong lĩnh vực tin tức.</li>
  <li style="margin-bottom: 0.05in;"><i>Fake News Detection Using BERT Model with Handcrafted Features</i> (IEEE, 2021): Công trình đã chứng minh tính hiệu quả của kiến trúc Hybrid khi trích xuất vector ngữ nghĩa từ mạng LLM (BERT) kết nối trực tiếp với ma trận đặc trưng thủ công (số lượng ký tự in hoa, dấu chấm than), giúp cải thiện rõ rệt độ chính xác của phân loại nhị phân.</li>
</ul>

<h3>2.3.3. So sánh tính ưu việt của đồ án (ShieldAI) so với các hệ thống hiện tại</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Dựa trên bức tranh tổng quan của các nghiên cứu đi trước, đồ án <b>ShieldAI</b> không chỉ kế thừa mà còn giải quyết được những hạn chế cốt lõi của các hệ thống phát hiện tin giả truyền thống. Dưới đây là bảng so sánh làm nổi bật tính tối ưu (Optimization) và sự phát triển của đồ án:</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>1. Khả năng Nắm bắt Ngôn ngữ</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Hệ thống đoạt giải VLSP ReINTEL Challenge 2020:</b> Sử dụng PhoBERT kết hợp với Ensemble Learning chạy trên tập dữ liệu tổng hợp. Tuy đạt điểm số thi đấu cao nhưng cấu trúc này dễ bị thiếu sót từ vựng khi áp dụng vào các bài báo y khoa có thuật ngữ chuyên sâu.</li>
  <li style="margin-bottom: 0.05in;"><b>ShieldAI (Tính Khái quát hóa Cao):</b> Cũng kế thừa khả năng của <b>PhoBERT</b> và được huấn luyện trên bộ ngữ liệu tin y tế/sức khỏe tiếng Việt (<b>10.609 mẫu</b> sau lọc). Mô hình được trang bị khả năng hiểu rõ văn cảnh tiếng Việt, ngữ pháp tiếng lóng và các từ khóa thao túng tâm lý, hỗ trợ phát hiện các thủ đoạn lừa đảo tinh vi trên không gian mạng.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>2. Kiến trúc Mô hình</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Hệ thống đoạt giải VLSP ReINTEL Challenge 2020:</b> Xây dựng kiến trúc Ensemble kết hợp hàng loạt mạng Nơ-ron lớn với nhau. Mô hình này vô cùng cồng kềnh, chỉ nhằm mục đích lấy điểm số thi đấu cực hạn chứ hầu như không thể mang ra chạy thực tế vì tốn quá nhiều phần cứng.</li>
  <li style="margin-bottom: 0.05in;"><b>ShieldAI (Tối ưu Cấu trúc Text-only):</b> Thiết kế cấu trúc PhoBERT + MLP tinh gọn tối đa. Thay vì nối vector phức tạp, hệ thống chỉ trích xuất vector ngữ nghĩa 768 chiều từ PhoBERT, chuẩn hóa bằng StandardScaler và phân loại qua MLP (128, 64). Cơ chế Heuristics được tách rời thành Động cơ giải thích độc lập. Điều này giúp hệ thống đạt độ chuẩn xác ấn tượng mà vẫn nhẹ nhàng, chạy mượt mà trên môi trường Web.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>3. Tính Minh bạch (Explainability)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Hệ thống đoạt giải VLSP ReINTEL Challenge 2020:</b> Hoạt động như một "Hộp đen" (Black-box) 100%. Khi nhận đầu vào, mô hình chỉ xuất ra một tệp kết quả chứa nhãn "0" (Thật) hoặc "1" (Giả) mà không thể đưa ra bất kỳ lý do nào giải thích cho kết quả đó.</li>
  <li style="margin-bottom: 0.05in;"><b>ShieldAI (Tối ưu Niềm tin):</b> Tích hợp hệ thống <b>Động cơ Giải thích Heuristic</b> (rule-based). Phần mềm quét các tín hiệu hình thức trên văn bản gốc và in ra màn hình lý do cảnh báo (ví dụ: "Tiêu đề viết hoa quá nhiều" hay "Văn phong giật gân, thiếu tính trung lập"). Giúp người dùng thực sự tin tưởng vào phán quyết của AI.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>4. Trải nghiệm & Khả năng Vận hành Thực tế</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Hệ thống đoạt giải VLSP ReINTEL Challenge 2020:</b> Hoàn toàn không có giao diện người dùng (No UI) và không có khả năng tự lấy tin tức. Chỉ là một tệp mã nguồn chạy Offline nhập liệu thủ công trên máy tính cá nhân của nhà nghiên cứu.</li>
  <li style="margin-bottom: 0.05in;"><b>ShieldAI (Tối ưu Trải nghiệm):</b> Đóng gói mô hình AI thành một nền tảng phần mềm Client-Server hoàn chỉnh. Tích hợp <b>BeautifulSoup</b> (Web Crawler) tự động cào nội dung tin tức trực tiếp từ URL mạng trong tích tắc thay vì copy-paste thủ công. Backend sử dụng <b>FastAPI</b> bất đồng bộ (Asynchronous) kết hợp với Frontend <b>Next.js 14</b> và lưu trữ <b>SQLite</b> nhằm mang lại hiệu năng cao và UX/UI chuyên nghiệp. Đưa AI ra khỏi phòng thí nghiệm và sẵn sàng phục vụ người dùng cuối (End-user).</li>
</ul>
<h2>2.4. Công nghệ và Công cụ sử dụng</h2>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Đồ án này không chỉ dừng lại ở việc thiết kế một mô hình AI chạy trong môi trường nghiên cứu cô lập (Jupyter Notebook), mà được xây dựng thành một nền tảng phần mềm hoàn chỉnh theo kiến trúc Client-Server. Dưới đây là các công nghệ lõi được sử dụng để hiện thực hóa toàn bộ hệ thống:</p>

<h3>2.4.3. Thư viện Trí tuệ Nhân tạo và Xử lý Ngôn ngữ</h3>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>PyTorch &amp; Transformers:</b> PyTorch được dùng để chạy mô hình <b>PhoBERT-base</b> (embedding [CLS] 768 chiều) qua thư viện Hugging Face <code>Transformers</code>. Bộ phân loại <b>MLP</b> được huấn luyện và suy luận bằng <code>scikit-learn</code> (<code>MLPClassifier</code> + <code>StandardScaler</code>), lưu artifact dạng <code>.joblib</code>.</li>
  <li style="margin-bottom: 0.05in;"><b>HuggingFace Transformers:</b> Là thư viện tiêu chuẩn toàn cầu trong lĩnh vực Xử lý ngôn ngữ tự nhiên. Thư viện này cho phép hệ thống nạp trực tiếp kiến trúc <code>vinai/phobert-base-v2</code> kèm theo trọng số (pre-trained weights) và Tokenizer chuẩn xác của nhóm nghiên cứu VinAI, giúp tiết kiệm hàng ngàn giờ huấn luyện lại từ đầu.</li>
  <li style="margin-bottom: 0.05in;"><b>PyVi (Python Vietnamese Toolkit):</b> Đặc thù của tiếng Việt là cấu trúc từ ghép (ví dụ: &quot;sinh viên&quot; là một từ có nghĩa thay vì hai từ đơn). Để mô hình PhoBERT [1] không bị hiện tượng thiếu hụt từ vựng (Out-of-Vocabulary), thư viện PyVi (module <code>ViTokenizer</code>) được hệ thống sử dụng độc quyền trong pipeline tiền xử lý để tự động nối các từ ghép bằng dấu gạch dưới (ví dụ: &quot;sinh_viên&quot;), đảm bảo tính toàn vẹn về mặt ngữ nghĩa trước khi chuyển đổi thành vector.</li>
  <li style="margin-bottom: 0.05in;"><b>Scikit-Learn & Pandas:</b> Thư viện Pandas cung cấp cấu trúc <code>DataFrame</code> giúp việc làm sạch và thao tác trên hàng chục ngàn dòng dữ liệu huấn luyện trở nên cực kỳ tối ưu. Scikit-Learn được sử dụng để tính toán các ma trận đánh giá hiệu năng (Confusion Matrix, F1-Score) và hỗ trợ chia tách tập dữ liệu (train/validation/test split) một cách ngẫu nhiên và phân tầng (stratified).</li>
</ul>

<h2>2.5. Biện luận lựa chọn kiến trúc AI</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Dựa trên các phân tích lý thuyết, mục này sẽ đưa ra các luận điểm chuyên sâu nhằm giải thích rõ lý do tại sao các công nghệ lõi lại được lựa chọn cho đồ án, đồng thời so sánh trực tiếp với các phương pháp truyền thống để làm nổi bật tính tối ưu của hệ thống.</p>

<h3>2.5.1. Lựa chọn Mô hình Ngôn ngữ Lõi (PhoBERT)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Hệ thống quyết định sử dụng <b>PhoBERT</b> (mô hình Transformer dành riêng cho tiếng Việt) thay vì các thuật toán Machine Learning truyền thống (SVM, Naive Bayes) hay Multilingual BERT (mBERT). Tiếng Việt có cấu trúc ngữ pháp đặc thù (từ ghép, từ mượn, tiếng lóng mạng). Việc PhoBERT được huấn luyện sẵn (pre-trained) trên kho dữ liệu 20GB văn bản tiếng Việt giúp mô hình nắm bắt ngữ cảnh và hàm ý sâu xa của câu chữ. Nếu so sánh, phương pháp TF-IDF kết hợp SVM tuy chạy rất nhanh nhưng "mù" hoàn toàn về mặt ngữ cảnh, dễ dàng bị đánh lừa bởi các thủ thuật lách luật. Trong khi đó, mBERT dù hỗ trợ đa ngôn ngữ nhưng vốn từ tiếng Việt lại quá mỏng. Do đó, PhoBERT là sự lựa chọn tối ưu nhất về mặt độ chính xác (Accuracy).</p>

<h3>2.5.2. Lựa chọn Kiến trúc PhoBERT + MLP (Text-only)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Đồ án áp dụng kiến trúc tinh gọn <b>PhoBERT Text-only + MLP</b>. Thay vì dung hợp rườm rà, mô hình chỉ sử dụng vector ngữ nghĩa của PhoBERT (768 chiều) làm đầu vào cho mạng Nơ-ron Truyền thẳng (MLP) có cấu trúc lớp ẩn (128, 64). Việc sử dụng một luồng đặc trưng giúp dễ dàng quản lý pipeline, giảm thiểu chi phí tính toán và tận dụng được sức mạnh tuyệt đối của PhoBERT trong việc nắm bắt ngữ cảnh. Các đặc trưng hình thức (Heuristics) được tách hẳn ra thành một phân hệ Động cơ Giải thích (Explanation Engine) độc lập chạy sau khi phân loại. Cách tiếp cận phân tách này giúp đạt F1-Score ấn tượng (93.71%) mà không cần phức tạp hóa mạng nơ-ron.</p>

<h3>2.5.3. Lựa chọn cơ chế giải thích dựa trên đặc trưng</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Trong nhiều hệ thống học sâu hiện nay, kết quả phân loại thường được cung cấp dưới dạng nhãn dự đoán mà không đi kèm thông tin giải thích, gây khó khăn cho người dùng trong việc đánh giá mức độ tin cậy của kết quả. Để khắc phục hạn chế này, đề tài xây dựng Động cơ giải thích rule-based độc lập (Explanation Engine) chạy hoàn toàn bên ngoài mạng nơ-ron lõi.</p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Động cơ này hoạt động bằng cách đo lường trực tiếp các tập đặc trưng Heuristics trên văn bản thô, bao gồm các chỉ số như tỷ lệ chữ in hoa, mật độ dấu câu, độ dài tiêu đề. Dựa trên các tập luật (rules) được lập trình sẵn, nó sẽ tự động biên dịch các chỉ số bất thường này thành những câu văn tiếng Việt thân thiện (ví dụ: "Lạm dụng dấu câu quá mức"). Các câu văn giải thích này được hiển thị đồng thời cùng với dự đoán xác suất, giúp minh bạch hóa lý do cảnh báo tin giả.</p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Sự tách biệt hoàn toàn giữa Toán học (dự đoán bằng PhoBERT) và Heuristics (giải thích bằng luật) đảm bảo tốc độ suy luận cực nhanh, giải quyết được bài toán "hộp đen" mà vẫn rất dễ dàng triển khai thực tế trên môi trường Web.</p>

<h2>2.6. Kết luận chương</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Chương 2 đã cung cấp một khung lý thuyết toàn diện và vững chắc, làm nền tảng khoa học cho toàn bộ quá trình thiết kế và phát triển hệ thống phát hiện tin giả. Thông qua việc phân tích chuyên sâu, đồ án đã làm rõ sự ưu việt của kiến trúc mạng nơ-ron Transformer [6, 7], đặc biệt là sức mạnh nắm bắt ngữ nghĩa tiếng Việt của mô hình ngôn ngữ lớn PhoBERT. Bên cạnh đó, việc khảo lược các công trình nghiên cứu tiên phong trong và ngoài nước đã khẳng định sự đúng đắn của phương pháp tiếp cận mạng đa tầng (PhoBERT Text-only + MLP) nhằm tối đa hóa độ chuẩn xác. Hơn nữa, việc nghiên cứu các cơ sở lý thuyết về Động cơ Giải thích độc lập (Rule-based Explanation) [5, 8] và hệ thống hóa toàn bộ công nghệ phát triển Web (FastAPI, Next.js, PyTorch) đã tạo ra một bức tranh toàn cảnh về mặt kỹ thuật. Những luận điểm lý thuyết và sự chuẩn bị về mặt công nghệ trong chương này chính là tiền đề quan trọng, định hướng trực tiếp cho các quyết định kiến trúc cốt lõi sẽ được thiết kế và mô hình hóa trong Chương 3 tiếp theo.</p>
<h1 style="page-break-before: always">CHƯƠNG 3: PHƯƠNG PHÁP
NGHIÊN CỨU VÀ THIẾT KẾ HỆ THỐNG</h1>
<h2>3.1. Phương pháp nghiên cứu</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để giải quyết bài toán phát hiện tin giả tiếng Việt, đồ án không áp dụng một thuật toán học máy đơn lẻ mà xây dựng một quy trình luận giải đa tầng (Multi-tier Analytical Pipeline). Phương pháp nghiên cứu được chia thành bốn mũi nhọn chiến lược, đi từ khâu thu thập dữ liệu thô, trích xuất đặc trưng, mô hình hóa suy luận, cho đến việc minh bạch hóa kết quả.</p>

<h3>3.1.1. Phân tích Dữ liệu nghiên cứu (Dataset Analysis)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mọi hệ thống Trí tuệ Nhân tạo đều được định hình bởi chất lượng của nguồn dữ liệu huấn luyện. Đồ án sử dụng bộ dữ liệu <b>"Vietnamese Fake News Dataset"</b> tổng hợp từ nhiều nguồn tin tức trên không gian mạng. Quá trình Khai phá và Phân tích Dữ liệu (Exploratory Data Analysis - EDA) đã chỉ ra các đặc tính học thuật quan trọng sau:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Số lượng mẫu và Phân bố nhãn (Label Distribution):</b> Bộ dữ liệu <code>full_dataset.csv</code> bao gồm tổng cộng <b>10.617 bản ghi (bài báo)</b>; sau lọc (<code>dataset_cleaner.py</code>) còn <b>10.609 mẫu</b> hợp lệ. Phân bố nhãn tương đối cân bằng (~53,6% tin thật / ~46,4% tin giả), giúp giảm rủi ro mô hình bị thiên lệch (class imbalance) trong quá trình huấn luyện.</li>
  <li style="margin-bottom: 0.05in;"><b>Độ dài văn bản và Hiện tượng Mất cân bằng dữ liệu:</b> Các bài viết lừa đảo thường sử dụng từ ngữ thao túng kết hợp với cấu trúc câu giật gân, đe dọa. Qua thống kê độ dài trên 10.609 mẫu, dữ liệu không có sự chênh lệch quá lớn về số lượng từ giữa tin thật và tin giả, đảm bảo mô hình không học vẹt theo độ dài văn bản.</li>
  <li style="margin-bottom: 0.05in;"><b>Cấu trúc trường thông tin:</b> Dữ liệu cung cấp các cột <code>title</code>, <code>content</code>, <code>url</code>, <code>source</code> phục vụ huấn luyện và crawl inference. Các tín hiệu hình thức (viết hoa, dấu câu) chỉ được dùng trong <code>ExplanationEngine</code> (XAI), không đưa vào vector đặc trưng mô hình.</li>
</ul>

<h3>3.1.2. Tiền xử lý và Làm sạch Dữ liệu (Data Cleaning)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Train và inference dùng chung hàm <code>preprocess_text</code> trong <code>text_utils.py</code> — tránh lệch pipeline. Các bước:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Chuẩn hóa chữ thường (lowercase):</b> Thống nhất biểu diễn văn bản.</li>
  <li style="margin-bottom: 0.05in;"><b>Loại bỏ URL:</b> Regex xóa liên kết <code>http(s)://...</code> không mang ngữ nghĩa phân loại.</li>
  <li style="margin-bottom: 0.05in;"><b>Chuẩn hóa khoảng trắng:</b> Gom nhiều khoảng trắng thành một, loại bỏ khoảng trắng thừa.</li>
  <li style="margin-bottom: 0.05in;"><b>Tách từ PyVi:</b> <code>ViTokenizer</code> nối từ ghép bằng dấu gạch dưới (ví dụ: <code>tin_giả</code>, <code>y_tế</code>) trước khi đưa vào PhoBERT.</li>
</ul>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><i>Lưu ý:</i> Module helper <code>TextCleaner</code> có thêm xóa HTML/teencode nhưng <b>không</b> nằm trên luồng <code>preprocess_text</code> chính. Crawler HTML chỉ dùng khi người dùng nhập URL (BeautifulSoup trích title/content).</p>
<h3>3.1.3. Phân chia Dữ liệu Huấn luyện (Data Split)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Do quy mô dữ liệu khổng lồ, tập dữ liệu được phân chia theo tỷ lệ <b>70% (Train) - 30% (Test)</b> để phục vụ cho các vòng đời của mô hình AI. Đặc biệt, kỹ thuật phân tầng (Stratified Split) được áp dụng nghiêm ngặt trong hàm <code>train_test_split</code> của thư viện Scikit-learn để đảm bảo tỷ lệ phân bố nhãn luôn được giữ nguyên. Ngoài ra, để tăng tính thuyết phục học thuật, đồ án còn áp dụng thêm kỹ thuật <b>Kiểm định chéo 5-Fold (Cross-validation)</b> trên tập Train. Việc tạo ra tập Test hoàn toàn biệt lập (chiếm tới 30% dữ liệu) là cơ chế phòng vệ cốt lõi để loại trừ hiện tượng Rò rỉ dữ liệu (Data Leakage), đảm bảo độ tin tuyệt đối của các chỉ số hiệu năng cuối cùng.</p>

<h3>3.1.4. Phương pháp Trích xuất đặc trưng đa chiều (Multi-dimensional Feature Extraction)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Nhận định rằng tin giả không chỉ sai lệch về mặt nội dung mà còn mang các dấu hiệu lừa đảo về mặt hình thức, đồ án phân định rõ ràng hai luồng xử lý độc lập:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Luồng Phân loại Ngữ nghĩa (Semantic Features):</b> Sử dụng mô hình PhoBERT [1] để ánh xạ văn bản thành không gian vector (embedding) 768 chiều duy nhất. Phương pháp này nắm bắt sự tương quan ngữ cảnh sâu xa giữa các từ để mạng MLP đưa ra dự đoán xác suất giả mạo.</li>
  <li style="margin-bottom: 0.05in;"><b>Luồng Giải thích Kinh nghiệm (Heuristics):</b> Chạy độc lập sau khi có xác suất phân loại. Hệ thống đo lường các tín hiệu hình thức (Non-textual signals) thông qua luật (Rule-based) để sinh ra câu văn giải thích. Các chỉ số này bao gồm: Độ dài tiêu đề, Tỷ lệ chữ IN HOA, Số lượng dấu chấm than (!), dấu hỏi (?) và Mật độ dấu câu tổng thể.</li>
</ul>

<h3>3.1.5. Phương pháp Mô hình hóa mạng đa tầng (PhoBERT + MLP)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Trái tim của hệ thống là phương pháp <b>PhoBERT Text-only + MLP</b>. Bộ phân loại là <code>sklearn.neural_network.MLPClassifier</code> (lớp ẩn 128, 64; ReLU; Adam; <code>alpha=0.1</code>; <code>early_stopping=True</code>). Vector ngữ nghĩa 768 chiều từ PhoBERT được trích xuất, chuẩn hóa bằng <code>StandardScaler</code> rồi đưa vào MLP. Heuristics không nối vào pipeline phân loại — chỉ dùng trong <code>ExplanationEngine</code> sau bước suy luận.</p>

<h3>3.1.6. Phương pháp Đánh giá và Giải thích (Explainability Integration)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Về mặt đánh giá, hệ thống áp dụng phương pháp Validation phân tầng (Stratified K-Fold) và sử dụng chỉ số F1-Score làm thước đo cốt lõi. Đề tài tích hợp <b>ExplanationEngine</b> rule-based: sau khi MLP trả xác suất, module quét văn bản gốc (viết hoa, dấu câu giật gân, độ dài tiêu đề…) và sinh câu giải thích tiếng Việt — không dùng SHAP/LIME hay gradient ngược trên trọng số MLP.</p>
<h2>3.2. Công nghệ triển khai hệ thống phần mềm</h2>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in; text-indent: 0.5in">Phần này trình bày các công nghệ kỹ thuật phần mềm được lựa chọn để hiện thực hóa mô hình AI thành một ứng dụng hoàn chỉnh.</p>



<h2 style="page-break-before: always">3.3. Phân tích yêu cầu</h2>
<div style="background-color: #f8f9fa; border-left: 4px solid #6c757d; padding: 10px; margin-bottom: 15px;">
  <i><b>*Lưu ý của tác giả:</b> Do tính chất và phạm vi của một đồ án Trí tuệ Nhân tạo, phần phân tích yêu cầu dưới đây chỉ được thiết kế ở mức độ cơ bản nhất để phục vụ cho việc kiểm thử mô hình Học máy, không đặt nặng tiêu chuẩn kỹ nghệ phần mềm.</i>
</div>
<h3>3.3.1. Yêu cầu chức năng</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Dựa trên mục tiêu nghiên cứu và bối cảnh sử dụng thực tế, hệ thống phát hiện tin giả được thiết kế với các yêu cầu chức năng cốt lõi (Bảng 3.1), chia làm 5 phân hệ (Module) chi tiết như sau:</p>

<p align="center" style="margin-top: 0.2in; font-style: italic; margin-bottom: 0.05in;">Bảng 3.1. Yêu cầu chức năng hệ thống ShieldAI</p>
<table width="100%" border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; border: 1px solid #000; font-size: 0.95em;">
  <tr style="background-color: #f2f2f2; font-weight: bold;">
    <td style="border: 1px solid #000; width: 8%; text-align: center;">Mã</td>
    <td style="border: 1px solid #000; width: 22%;">Yêu cầu</td>
    <td style="border: 1px solid #000;">Mô tả</td>
  </tr>
  <tr><td style="border: 1px solid #000; text-align: center;">FR-01</td><td style="border: 1px solid #000;">Nhập văn bản</td><td style="border: 1px solid #000;">Người dùng dán tiêu đề và nội dung bài viết</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">FR-02</td><td style="border: 1px solid #000;">Nhập URL</td><td style="border: 1px solid #000;">Crawl và trích xuất title/content từ báo điện tử</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">FR-03</td><td style="border: 1px solid #000;">Tiền xử lý</td><td style="border: 1px solid #000;"><code>preprocess_text</code>: lowercase, xóa URL, PyVi tokenize (luồng train/inference)</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">FR-04</td><td style="border: 1px solid #000;">Trích đặc trưng</td><td style="border: 1px solid #000;">PhoBERT embedding [CLS] 768 chiều</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">FR-05</td><td style="border: 1px solid #000;">Phân loại</td><td style="border: 1px solid #000;">Xác suất tin giả; verdict 3 mức (&lt;35% / 35–74% / ≥75%)</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">FR-06</td><td style="border: 1px solid #000;">Giải thích</td><td style="border: 1px solid #000;"><code>ExplanationEngine</code> rule-based, JSON tiếng Việt</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">FR-07</td><td style="border: 1px solid #000;">Lịch sử &amp; xác thực</td><td style="border: 1px solid #000;">JWT; lưu/xem lịch sử phân tích</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">FR-08</td><td style="border: 1px solid #000;">API REST</td><td style="border: 1px solid #000;"><code>/api/analyze</code>, <code>/api/health</code>, <code>/api/auth/*</code></td></tr>
</table>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>1. Phân hệ Quản lý Tài khoản (User Management)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Đăng ký và Đăng nhập:</b> Hệ thống cho phép người dùng tạo tài khoản mới và đăng nhập thông qua cơ chế xác thực an toàn.</li>
  <li style="margin-bottom: 0.05in;"><b>Quản lý Phiên (Session):</b> Cấp phát mã thông báo (Token JWT) để duy trì phiên làm việc của người dùng mà không cần lưu trữ mật khẩu trực tiếp.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>2. Phân hệ Thu thập &amp; Tiền xử lý Dữ liệu (Data Scraping &amp; Preprocessing)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Đầu vào Đa dạng:</b> Chức năng cho phép người dùng kiểm tra thông tin bằng 2 cách: (1) Nhập trực tiếp đoạn văn bản thô, hoặc (2) Cung cấp đường dẫn mạng (URL) của bài báo cần kiểm chứng.</li>
  <li style="margin-bottom: 0.05in;"><b>Trích xuất tự động (Web Scraping):</b> Khi người dùng nhập URL, hệ thống phải tự động truy cập, bóc tách chính xác thành phần Tiêu đề (Title) và Nội dung bài báo (Content). Chức năng này phải có bộ lọc thông minh để loại bỏ hoàn toàn các mã HTML thừa như menu điều hướng, quảng cáo, hay thẻ script.</li>
  <li style="margin-bottom: 0.05in;"><b>Chuẩn hóa Ngôn ngữ:</b> Áp dụng <code>preprocess_text</code>: lowercase → xóa URL → chuẩn hóa khoảng trắng → PyVi tokenize (ví dụ: "đại học" → "đại_học"). Cùng pipeline cho train và inference.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>3. Phân hệ Lõi: Suy luận bằng PhoBERT và Mạng nơ-ron đa tầng (Core Inference)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Trích xuất embedding:</b> Hệ thống trích vector [CLS] 768 chiều từ PhoBERT, chuẩn hóa bằng <code>StandardScaler</code> và phân loại qua MLP (scikit-learn).</li>
  <li style="margin-bottom: 0.05in;"><b>Suy luận tuần tự:</b> Luồng: thu thập văn bản → <code>preprocess_text</code> → PhoBERT embedding → MLP → verdict 3 mức → <code>ExplanationEngine</code> (rule-based, chạy sau phân loại).</li>
  <li style="margin-bottom: 0.05in;"><b>Phân loại và Cảnh báo (Verdict):</b> Đưa ra phán quyết cuối cùng dưới dạng 3 mức độ (Tin thật, Đáng ngờ, Tin giả) thay vì nhị phân cứng nhắc. Đánh giá này dựa trên chỉ số xác suất rủi ro (Confidence Score) từ 0% đến 100% do AI cung cấp.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>4. Phân hệ Trí tuệ Nhân tạo Minh bạch (Heuristic Explanation Engine - Giải thích Heuristic)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Phân tích tín hiệu hình thức:</b> <code>ExplanationEngine</code> đo các chỉ số rule-based (viết hoa, dấu câu giật gân, độ dài tiêu đề…) trên văn bản gốc và sinh câu giải thích — không phân tích ngược trọng số nội bộ MLP.</li>
  <li style="margin-bottom: 0.05in;"><b>Sinh Báo cáo Trực quan:</b> Trả về báo cáo dưới dạng JSON để Frontend hiển thị thành các thanh trạng thái (Progress Bars), giúp người dùng đọc hiểu dễ dàng tại sao bài báo lại bị dán nhãn lừa đảo.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>5. Phân hệ Quản lý Lịch sử (History Tracking)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Lưu trữ Lượt quét:</b> Tự động lưu lại toàn bộ các văn bản hoặc URL mà người dùng đã kiểm chứng vào cơ sở dữ liệu.</li>
  <li style="margin-bottom: 0.05in;"><b>Truy xuất Báo cáo cũ:</b> Cho phép người dùng xem lại kết quả phân loại và bảng báo cáo Heuristic của các bài báo cũ mà không cần phải bắt hệ thống phân tích lại từ đầu.</li>
</ul>
<h3>3.3.2. Yêu cầu phi chức năng</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để đảm bảo hệ thống không chỉ là một mô hình học máy chạy trên môi trường cục bộ (Local) mà có thể sẵn sàng phục vụ người dùng cuối trong môi trường sản xuất (Production), các yêu cầu phi chức năng (Non-Functional Requirements) được định nghĩa khắt khe qua 5 khía cạnh sau:</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>1. Hiệu suất và Độ trễ (Performance &amp; Latency)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Giới hạn thời gian phản hồi:</b> Đối với phương thức nhập URL, hệ thống hướng tới việc tối ưu hóa thời gian xử lý, đảm bảo độ trễ ở mức chấp nhận được trong môi trường thử nghiệm.</li>
  <li style="margin-bottom: 0.05in;"><b>Tải trọng đồng thời (Concurrency):</b> Backend (FastAPI) áp dụng cấu hình bất đồng bộ (Asynchronous) nhằm cải thiện khả năng chịu tải so với các framework đồng bộ truyền thống.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>2. Bảo mật và An toàn hệ thống (Security)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Bảo mật phiên làm việc:</b> Kiến trúc stateless với <b>JSON Web Token (JWT)</b>. API trả JSON thống nhất: HTTP <b>200</b> kèm trường <code>status</code> (<code>success</code> / <code>error</code>) và <code>message</code> — kể cả lỗi đăng nhập, thiếu JWT hay nội dung trống (frontend đọc <code>status</code>, không dựa mã 401/403).</li>
  <li style="margin-bottom: 0.05in;"><b>Mã hóa dữ liệu nhạy cảm:</b> Toàn bộ mật khẩu của người dùng khi đăng ký phải được băm một chiều bằng thuật toán <b>Bcrypt</b> trước khi ghi vào cơ sở dữ liệu (SQLite/PostgreSQL).</li>
  <li style="margin-bottom: 0.05in;"><b>Chống lạm dụng API:</b> Hệ thống phải tích hợp cơ chế hạn chế tốc độ (Rate Limiting) trên các endpoint phân tích để chống lại các cuộc tấn công từ chối dịch vụ (DDoS) hoặc việc bot spam URL liên tục.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>3. Khả năng mở rộng và Tính khả dụng (Scalability &amp; Availability)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Kiến trúc Tách rời (Decoupled Architecture):</b> Việc tách biệt hoàn toàn Frontend (Next.js) và Backend (FastAPI) qua giao tiếp RESTful API đảm bảo rằng việc cập nhật giao diện không làm ảnh hưởng đến lõi mô hình AI và ngược lại.</li>
  <li style="margin-bottom: 0.05in;"><b>Sẵn sàng đóng gói (Docker-ready):</b> Cấu trúc mã nguồn phải sẵn sàng cho việc đóng gói vào các Container (Docker), tạo tiền đề cho việc triển khai linh hoạt lên đám mây (Cloud) như AWS hay Heroku.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>4. Trải nghiệm người dùng (Usability &amp; UX)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Khả năng tương thích chéo (Responsive Design):</b> Giao diện Web phải hiển thị hiệu quả trên cả trình duyệt máy tính (Desktop) lẫn thiết bị di động (Mobile). Các biểu đồ phân tích phải được tối ưu kích thước để không bị tràn màn hình.</li>
  <li style="margin-bottom: 0.05in;"><b>Cảnh báo lỗi thân thiện (Graceful Error Handling):</b> Khi cào một URL thất bại (do trang báo chặn bot hoặc URL chết), hệ thống không được crash mà phải trả về một thông báo lỗi (Toast message) rõ ràng, dễ hiểu cho người dùng.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>5. Khả năng bảo trì và Nâng cấp mô hình (Maintainability &amp; MLOps)</b></p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Cấu trúc thư mục chuẩn:</b> Mã nguồn Python tuân cấu trúc tách module (<code>models/</code>, <code>api/</code>, <code>text_utils.py</code>, …); các hàm lõi có Docstring đầy đủ.</li>
  <li style="margin-bottom: 0.05in;"><b>Tách biệt artifact:</b> PhoBERT tải qua Hugging Face; MLP + StandardScaler lưu <code>.joblib</code> trong <code>models/</code>, không nhúng vào mã nguồn — dễ retrain mà không đổi logic Backend.</li>
</ul>
<h2>3.4. Thiết kế hệ thống</h2>
<h3>3.4.1. Kiến trúc hệ thống</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Dựa trên các yêu cầu đã phân tích, hệ thống được thiết kế theo kiến trúc <b>Client-Server (Front-end & Back-end Separation)</b> nhằm tối đa hóa khả năng bảo trì và tốc độ xử lý. Cụ thể, kiến trúc hệ thống được chia làm ba tầng (Tiers) chính như minh họa dưới đây:</p>

<p align="center" style="margin-top: 0.2in; margin-bottom: 0.2in;">
![Sơ đồ Kiến trúc Hệ thống 3 Tầng](image/kientruc.png)
<br><i>Sơ đồ Kiến trúc Hệ thống 3 Tầng</i>
</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Như minh họa trong sơ đồ trên, thay vì gộp chung mọi logic xử lý vào một khối nguyên khối (Monolith Architecture), đồ án đã áp dụng kiến trúc phân tán <b>3 tầng (3-Tier Micro-Architecture) độc lập</b> (cùng với 1 tầng lưu trữ). Việc chia tách này không chỉ giúp quản lý mã nguồn dễ dàng mà còn đảm bảo tính mở rộng (Scalability), tính tái sử dụng và bảo mật (Security) cho hệ thống trong môi trường thực tế. Sự giao tiếp giữa các tầng được kiểm soát chặt chẽ thông qua các chuẩn HTTP và dữ liệu JSON. Cụ thể, các tầng được thiết kế chi tiết như sau:</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Tầng 1: Tầng Giao diện Người dùng (Presentation / Client Tier)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Tầng Giao diện đóng vai trò là điểm chạm đầu tiên (touchpoint) giữa người dùng và hệ thống. Được xây dựng hoàn toàn bằng <b>Next.js 14</b> (một React Framework hiện đại) kết hợp cùng <b>Tailwind CSS</b> và thư viện chuyển động <b>Framer Motion</b>, tầng này đảm bảo trải nghiệm đa nền tảng (Responsive Design) và tương tác cực kỳ mượt mà từ màn hình máy tính đến thiết bị di động. Điểm cốt lõi trong thiết kế của Tầng Giao diện là nó hoàn toàn "mù" (agnostic) về các thuật toán Trí tuệ Nhân tạo phức tạp bên dưới. Nhiệm vụ của nó chỉ là tiếp nhận yêu cầu đầu vào từ người dùng (một đoạn văn bản nghi ngờ hoặc một đường dẫn URL bài báo), đóng gói thành các truy vấn chuẩn HTTP RESTful, và gửi đi. Khi nhận được kết quả trả về từ máy chủ, module <b>Trực quan hóa Dữ liệu</b> sẽ sử dụng các công cụ vẽ biểu đồ linh hoạt để kết xuất các thông số đánh giá một cách sinh động nhất (ví dụ: thanh tiến trình hiển thị 99% giả mạo, biểu đồ radar cho các chỉ số cảm xúc, hoặc bôi đỏ các từ ngữ giật gân). Cơ chế này giúp người dùng phổ thông, dù không có chuyên môn về máy học, vẫn có thể dễ dàng hiểu thấu đáo phán quyết của hệ thống.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Tầng 2: Tầng Xử lý Nghiệp vụ (Application / Backend Tier)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Đây là "trái tim điều phối" của toàn bộ nền tảng phần mềm, được triển khai bằng framework <b>FastAPI</b>. Các endpoint trả JSON với envelope <code>{"status": "success"|"error", "message": "...", ...}</code>; mã HTTP thường là <b>200</b> (kể cả lỗi nghiệp vụ như sai mật khẩu hoặc chưa đăng nhập). Ba phân hệ chính: (1) <b>JWT Auth</b>; (2) <b>Web Scraper</b> (BeautifulSoup khi nhập URL); (3) <b>Router</b> điều phối sang Tầng AI.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Tầng 3: Tầng Suy luận Trí tuệ Nhân tạo (AI Inference Tier)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Tầng này chứa pipeline suy luận ShieldAI: <b>PhoBERT</b> (PyTorch/Transformers) trích embedding [CLS] 768 chiều; <b>StandardScaler + MLPClassifier</b> (scikit-learn, file <code>.joblib</code>) tính xác suất tin giả; <code>verdict.py</code> quy đổi 3 mức. Sau đó <b>ExplanationEngine</b> (rule-based) quét văn bản gốc (in hoa, dấu câu giật gân…) để sinh JSON giải thích tiếng Việt — <b>không</b> tham gia phân loại.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Tầng 4: Tầng Lưu trữ Dữ liệu (Data Storage Tier)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mặc dù là tầng thấp nhất, Tầng Lưu trữ lại đóng vai trò tối quan trọng trong việc bảo toàn tính bền vững của nền tảng. Hệ thống sử dụng <b>SQLite</b> kết nối qua mô hình ORM của thư viện SQLAlchemy. Mọi kết quả phân tích JSON chi tiết từ Tầng AI, thông tin tài khoản người dùng, và lịch sử hoạt động đều được lưu vết vĩnh viễn tại đây. Cơ chế này đem lại lợi thế vô cùng to lớn: nó cho phép người dùng có thể tra cứu ngay lập tức các bài báo họ đã quét trong quá khứ thông qua bảng điều khiển cá nhân (Dashboard), mà không cần phải bắt các cụm GPU/CPU của hệ thống AI phải vất vả chạy lại các phép toán nặng nề cho một dữ liệu cũ.</p>
<h3>3.4.2. Thiết kế cơ sở dữ liệu và Mô hình Thực thể - Mối quan hệ (ERD)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để đảm bảo tính bền vững và nhất quán của luồng dữ liệu, hệ thống sử dụng hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) <b>SQLite</b> kết hợp cùng công nghệ ánh xạ đối tượng <b>SQLAlchemy ORM (Object-Relational Mapping)</b>. Việc lựa chọn SQLite được xem là một quyết định kiến trúc chiến lược: nó cung cấp một giải pháp lưu trữ cực kỳ nhẹ (lightweight), không đòi hỏi cấu hình máy chủ cơ sở dữ liệu phức tạp, nhưng vẫn tuân thủ đầy đủ các tiêu chuẩn ACID (Atomicity, Consistency, Isolation, Durability) để đảm bảo an toàn dữ liệu. Thay vì viết các câu lệnh SQL thô (Raw SQL) dễ gây ra lỗ hổng bảo mật SQL Injection, SQLAlchemy ORM cho phép thao tác với dữ liệu dưới dạng các đối tượng (Objects) trong Python, giúp mã nguồn sạch sẽ, trực quan và dễ bảo trì hơn rất nhiều.</p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mô hình Thực thể - Mối quan hệ (Entity-Relationship Diagram - ERD) của hệ thống được thiết kế theo hướng tinh gọn, tập trung chủ yếu vào việc giải quyết bài toán cốt lõi: lưu trữ định danh người dùng, vết tích của quá trình phân tích AI, và thu thập phản hồi của người dùng để liên tục cải thiện mô hình. Hệ thống bao gồm ba thực thể chính là bảng <code>USERS</code> (Người dùng), bảng <code>ANALYSIS_HISTORY</code> (Lịch sử phân tích) và bảng <code>FEEDBACKS</code> (Phản hồi).</p>

<p align="center" style="margin-top: 0.2in; margin-bottom: 0.2in;">
![Sơ đồ Thực thể - Mối quan hệ ERD](image/erd.png)
<br><i>Sơ đồ Thực thể - Mối quan hệ (ERD)</i>
</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Chi tiết về các bảng và cấu trúc trường (Fields) được phân tích như sau:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Bảng USERS (Quản lý Tài khoản):</b> Chịu trách nhiệm lưu trữ thông tin cá nhân. Trường <code>email</code> và <code>username</code> được đánh chỉ mục độc nhất (Unique Index) để làm định danh đăng nhập. Mật khẩu tuyệt đối không được lưu dưới dạng văn bản thô, mà sử dụng thuật toán băm một chiều để tạo ra trường <code>hashed_password</code> nhằm ngăn chặn rò rỉ dữ liệu.</li>
  <li style="margin-bottom: 0.05in;"><b>Bảng ANALYSIS_HISTORY (Lịch sử Phân tích):</b> Đây là quyển "Sổ cái" ghi lại chi tiết hoạt động của Động cơ AI. Bên cạnh các dữ liệu đầu vào như <code>input_mode</code> (URL/Text), <code>title</code>, <code>content</code>, bảng còn lưu trữ chi tiết phán quyết của AI thông qua <code>fake_prob</code> (xác suất) và <code>verdict</code> (3 ngưỡng cảnh báo). Đặc biệt, trường <code>explanation_json</code> và <code>meta_json</code> cho phép linh hoạt lưu trữ báo cáo Heuristics bán cấu trúc (NoSQL-like) ngay bên trong CSDL quan hệ.</li>
  <li style="margin-bottom: 0.05in;"><b>Bảng FEEDBACKS (Quản lý Phản hồi):</b> Đóng vai trò cực kỳ quan trọng trong chiến lược MLOps (Machine Learning Operations). Bảng cho phép người dùng đánh giá tính chính xác của phán quyết AI (<code>is_correct</code>) và để lại bình luận (<code>comment</code>). Dữ liệu này là nguồn tài nguyên quý giá để nhóm nghiên cứu tái huấn luyện (Re-train) mô hình trong tương lai.</li>
</ul>

<p align="center" style="margin-top: 0.2in; font-style: italic; margin-bottom: 0.05in;">Bảng 3.2. Từ điển Dữ liệu (Data Dictionary) cho các Thực thể</p>

<table width="100%" border="1" cellpadding="8" cellspacing="0" style="display: table; width: 100%; border-collapse: collapse; border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; table-layout: fixed; word-wrap: break-word; word-break: break-word; white-space: normal;">
  <tr style="background-color: #f2f2f2;">
    <th width="20%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Thực thể</th>
    <th width="20%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Trường dữ liệu</th>
    <th width="15%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Kiểu dữ liệu</th>
    <th width="45%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: left;">Mô tả chi tiết</th>
  </tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>USERS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>id</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Integer</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Khóa chính (PK), tự động tăng.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>USERS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>email</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(255)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Email đăng nhập (Unique, Index).</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>USERS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>username</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(64)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Tên người dùng hiển thị (Unique, Index).</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>USERS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>hashed_password</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(255)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Mật khẩu đã mã hóa.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>USERS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>created_at</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">DateTime</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Thời điểm khởi tạo tài khoản.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>id</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Integer</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Khóa chính (PK), tự động tăng.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>user_id</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Integer</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Khóa ngoại (FK) trỏ đến bảng USERS.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>input_mode</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(10)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Loại đầu vào: "text" hoặc "url".</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>title</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(500)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Tiêu đề bài báo (nếu có).</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>content</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Text</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Nội dung bài báo hoặc đoạn văn bản.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>source_url</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(2048)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">URL gốc của bài báo (nếu input_mode="url").</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>source_domain</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(255)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Tên miền gốc của URL (nếu có).</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>result_label</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(64)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Nhãn dự đoán cuối cùng.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>fake_prob</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Float</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Xác suất giả mạo từ AI (0.0 đến 1.0).</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>verdict</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">String(32)</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Ngưỡng cảnh báo (Tin Thật/Đáng ngờ/Tin Giả).</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>explanation_json</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Text</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Báo cáo giải thích minh bạch từ Heuristics.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>meta_json</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Text</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Thông tin siêu dữ liệu mở rộng.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>ANALYSIS_HISTORY</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>created_at</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">DateTime</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Thời gian phân tích.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>FEEDBACKS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>id</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Integer</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Khóa chính (PK), tự động tăng.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>FEEDBACKS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>history_id</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Integer</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Khóa ngoại (FK) trỏ 1-1 về bảng ANALYSIS_HISTORY.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>FEEDBACKS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>user_id</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Integer</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Khóa ngoại (FK) trỏ về bảng USERS.</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>FEEDBACKS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>is_correct</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Boolean</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Đánh giá dự đoán có chính xác không (Thumbs up/down).</td></tr>
  <tr><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><b>FEEDBACKS</b></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;"><code>comment</code></td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Text</td><td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Nhận xét chi tiết từ người dùng (nếu có).</td></tr>
</table>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mối quan hệ giữa các thực thể này là mối quan hệ <b>1-N (Một - Nhiều)</b> giữa người dùng với lịch sử phân tích, và quan hệ <b>1-1 (Một - Một)</b> giữa bản phân tích và một phản hồi duy nhất. Việc ứng dụng ORM SQLAlchemy giúp liên kết tường minh thông qua các khóa ngoại (Foreign Keys). Khái niệm này phản ánh luồng nghiệp vụ thực tế: Một người dùng quét nhiều bài báo, họ đánh giá các báo cáo này, và toàn bộ dữ liệu trở thành quy mô tri thức mới khổng lồ để cải thiện AI trong tương lai.</p>
<h3>3.4.3. Thiết kế giao diện (UI/UX Design) và Trải nghiệm Người dùng</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Với mục tiêu đưa công nghệ Trí tuệ Nhân tạo phức tạp đến gần hơn với người dùng phổ thông, Giao diện người dùng (User Interface - UI) và Trải nghiệm người dùng (User Experience - UX) của hệ thống được thiết kế theo triết lý <b>Tối giản và Hiện đại (Modern Minimalism)</b>. Toàn bộ nền tảng Frontend được xây dựng bằng Next.js kết hợp với bộ công cụ <b>Tailwind CSS</b>. Việc ứng dụng Tailwind giúp hệ thống duy trì được một cấu trúc mã màu (Color Palette) nhất quán, áp dụng chuẩn thiết kế bo góc (border-radius mềm mại), hiệu ứng kính mờ (Glassmorphism), và đặc biệt là khả năng tương thích hiển thị hiệu quả trên mọi kích thước màn hình (Fully Responsive) từ màn hình Desktop rộng lớn cho đến điện thoại di động. Tổng thể giao diện hệ thống bao gồm ba phân hệ màn hình cốt lõi, mỗi phân hệ được thiết kế để giải quyết một điểm chạm cụ thể của người dùng:</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>1. Màn hình Cổng thông tin và Phân tích (Home & Analysis Portal)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Đây là màn hình đầu tiên khi người dùng truy cập vào ứng dụng. Thiết kế tập trung hoàn toàn sự chú ý của người dùng vào một <b>Thanh tìm kiếm (Search Bar)</b> kích thước lớn đặt ở chính giữa không gian làm việc. Thanh tìm kiếm này được thiết kế thông minh với tính năng đa định dạng đầu vào (Multi-input format): người dùng có thể dán (paste) trực tiếp một đường dẫn URL của bài báo mạng, hoặc gõ một đoạn văn bản thô bất kỳ vào khung soạn thảo. Ngay phía dưới là nút "Phân tích nội dung" được tích hợp các hiệu ứng vi mô (micro-interactions) phản hồi xúc giác khi rê chuột (hover). Trong quá trình chờ máy chủ chạy các phép toán AI, màn hình sẽ hiển thị các hiệu ứng tải (Loading animations) dạng sóng mượt mà, giúp xoa dịu và giảm thiểu cảm giác chờ đợi của người dùng (UX optimization).</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>2. Màn hình Báo cáo Giám định (Result & Giải thích Heuristic Dashboard)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Màn hình báo cáo kết quả chính là nơi trình diễn toàn bộ khả năng của công nghệ Trí tuệ Nhân tạo Minh bạch (Heuristic Explanation). Khác với các hệ thống truyền thống chỉ hiện một dòng chữ khô khan, màn hình này áp dụng nguyên lý thiết kế <b>Thị giác hóa mức độ rủi ro (Visual Risk Assessment)</b> thông qua mã màu: <span style="color: red; font-weight: bold;">Màu Đỏ/Cam</span> sẽ chớp cảnh báo cho các tin giả độc hại và <span style="color: green; font-weight: bold;">Màu Xanh lá cây</span> sẽ đại diện cho nguồn thông tin an toàn, đáng tin cậy. Giao diện được chia bố cục làm hai vùng chính (Grid Layout):</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Vùng Chỉ số Tổng quan:</b> Hiển thị một vòng tròn đo lường tỷ lệ phần trăm (Confidence Score) cực lớn, giúp người dùng nắm bắt ngay kết luận cuối cùng (ví dụ: "Bài báo này 94% là Giả mạo") chỉ trong vòng 2 giây đầu tiên lướt nhìn.</li>
  <li style="margin-bottom: 0.05in;"><b>Vùng Phân tích Chuyên sâu (Giải thích Heuristic Metrics):</b> Đây là khu vực mang lại giá trị cốt lõi nhất, nơi hiển thị các thanh đo (Progress bars) bóc tách chi tiết lý do tại sao văn bản lại bị AI đánh dấu như vậy. Các chỉ số như "Tỷ lệ lạm dụng viết hoa", "Mật độ sử dụng dấu chấm than", "Số lượng từ lóng", hay "Chỉ số cảm xúc tiêu cực" được trực quan hóa sinh động. Nhờ tận dụng cấu trúc Component của React, các thanh đồ thị này được thiết lập hiệu ứng chạy mượt mà từ 0% lên đến mức thực tế, tạo cho người dùng một cảm giác thỏa mãn khi thấy hệ thống đang "suy nghĩ" và giải trình rất minh bạch ngay trước mắt họ.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>3. Màn hình Quản lý Lịch sử (Personal History View)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để tăng tính gắn kết cá nhân hóa, hệ thống cung cấp một bảng điều khiển lưu trữ toàn bộ các phiên phân tích trong quá khứ của người dùng. Màn hình này áp dụng thiết kế dạng danh sách thẻ động (Dynamic Cards), cho phép người dùng lướt nhanh qua các tiêu đề bài báo đã quét, thời gian thực hiện thao tác và đóng dấu nhãn Thật/Giả một cách rõ ràng. Điểm tối ưu về mặt UI/UX ở đây là việc triển khai tính năng phân trang (Pagination) ngay tại phía máy chủ kết hợp bộ lọc động, giúp giao diện Frontend có thể tải và cuộn qua hàng trăm bản ghi lịch sử một cách cực kỳ nhẹ nhàng, không gây tràn bộ nhớ (RAM) hay giật lag trình duyệt của người dùng.</p>
<h3>3.4.4. Thiết kế thuật toán (Thuật toán PhoBERT + MLP - PhoBERT + MLP)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Đồ án triển khai thuật toán <b>PhoBERT Text-only + MLP</b>. Phân loại dựa hoàn toàn trên embedding ngữ nghĩa 768 chiều; giải thích rule-based chạy <b>sau</b> bước phân loại, không ghép (concatenate) đặc trưng hình thức vào MLP. Lưu đồ dưới đây mô tả luồng từ văn bản đầu vào đến verdict và báo cáo giải thích.</p>

<p align="center" style="margin-top: 0.2in; margin-bottom: 0.2in;"><img src="image/luong_xu_ly.png" style="width: 80%; max-width: 600px; border: 1px solid #ccc;"></p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Theo lưu đồ trên, thuật toán chạy theo pipeline tuần tự: tiền xử lý → embedding → phân loại → giải thích. Chi tiết các bước:</p>

<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Bước 1: Tiền xử lý (Preprocessing):</b> Áp dụng <code>preprocess_text</code>: lowercase → xóa URL → chuẩn hóa khoảng trắng → PyVi tokenize. Cùng logic cho train và inference.</li>
  <li style="margin-bottom: 0.05in;"><b>Bước 2: Giải mã Ngữ nghĩa (PhoBERT):</b> Văn bản sạch được đưa qua bộ Tokenizer của PhoBERT để băm nhỏ thành các mảnh từ vựng (Sub-words). Sau đó, chuỗi token này đi xuyên qua 12 lớp Mạng Tự chú ý (Self-Attention) của kiến trúc Transformer [6, 7]. Kết quả trả về là một siêu vector đặc trưng đại diện toàn cục cho ngữ cảnh của câu (thường gọi là <code>[CLS] token vector</code>), có kích thước cực lớn lên đến <b>768 chiều</b>. Vector này nắm giữ toàn bộ "ý nghĩa sâu xa" và "giọng điệu mỉa mai" ẩn giấu trong bài báo.</li>
  <li style="margin-bottom: 0.05in;"><b>Bước 3: Phân loại (StandardScaler + MLPClassifier):</b> Vector 768 chiều được <code>StandardScaler</code> chuẩn hóa, đưa vào <code>MLPClassifier</code> (128, 64). <code>predict_proba</code> trả xác suất tin giả; <code>verdict.py</code> quy đổi 3 mức: &lt;35% tin thật, 35–74% đáng ngờ, ≥75% tin giả.</li>
  <li style="margin-bottom: 0.05in;"><b>Bước 4: Giải thích (ExplanationEngine):</b> Module rule-based quét văn bản gốc (viết hoa, dấu chấm than, văn phong giật gân), kết hợp xác suất từ MLP để sinh JSON giải thích tiếng Việt.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để minh họa logic lập trình, luồng suy luận được tổng hợp thành đoạn Mã giả (Pseudocode) sau:</p>

<pre style="white-space: pre-wrap; font-family: monospace; background-color: #f5f5f5; padding: 10px; border: 1px solid #ccc; line-height: 1.5; overflow-x: auto;"><code>ALGORITHM: PhoBERT Text-only MLP Inference &amp; Rule-based Explanation
INPUT:
    T: Văn bản gốc hoặc URL bài viết
OUTPUT:
    Verdict (Tin Thật/Đáng ngờ/Tin Giả), Confidence_Score, Explanation_Report

BEGIN
    // Bước 1: Tiền xử lý (preprocess_text)
    IF T is URL THEN
        T = CRAWL_AND_EXTRACT(T)   // BeautifulSoup: title + content
    END IF
    T_clean = PREPROCESS_TEXT(T) // lowercase, xóa URL, whitespace, PyVi

    // Bước 2: Trích xuất embedding PhoBERT (PyTorch/Transformers)
    Tokens = PHOBERT_TOKENIZER(T_clean)
    V_phobert = PHOBERT_MODEL(Tokens).extract_CLS()  // Vector [CLS] 768 chiều
    V_scaled = STANDARD_SCALER.transform(V_phobert)

    // Bước 3: Phân loại (sklearn MLPClassifier)
    Confidence_Score = MLP_CLASSIFIER.predict_proba(V_scaled)[1]  // xác suất tin giả

    // Bước 4: Verdict 3 mức (verdict.py)
    Verdict = MAP_TO_VERDICT(Confidence_Score)  // &lt;0.35 / 0.35–0.74 / ≥0.75

    // Bước 5: Giải thích rule-based (ExplanationEngine)
    Explanation_Report = EXPLANATION_ENGINE(T, Confidence_Score, Verdict)
    // Quét văn bản gốc: viết hoa, dấu câu, văn phong giật gân → JSON tiếng Việt

    RETURN Verdict, Confidence_Score, Explanation_Report
END</code></pre>

<h2>3.5. Kết luận chương</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Chương 3 đóng vai trò là bản lề định hình toàn bộ khung xương kỹ thuật của đồ án, chuyển tiếp từ các lý thuyết nền tảng (Chương 2) sang một bản thiết kế hệ thống phần mềm hoàn chỉnh và sẵn sàng để lập trình thực tế. Nhìn lại toàn bộ chương, đồ án đã giải quyết ba bài toán cốt lõi trong việc xây dựng một hệ thống Trí tuệ Nhân tạo ứng dụng thực tiễn:</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Thứ nhất, về mặt Kiến trúc Phần mềm:</b> Đồ án thiết kế hệ thống theo kiến trúc <b>Micro-Architecture 3 tầng (3-Tier) độc lập</b>. Việc chia tách Tầng Giao diện (Next.js), Tầng Nghiệp vụ (FastAPI) và Tầng Suy luận AI (PhoBERT + MLP) đảm bảo tính bảo mật, khả năng mở rộng và chịu tải trong môi trường mạng thực tế.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Thứ hai, về mặt Thiết kế Dữ liệu và Trải nghiệm:</b> Việc ứng dụng linh hoạt giữa mô hình quan hệ chặt chẽ (SQLite/SQLAlchemy) và định dạng dữ liệu bán cấu trúc (JSON) trong lưu trữ báo cáo Heuristic cho thấy sự tối ưu hóa cao độ về mặt lưu trữ truy vấn. Song song đó, triết lý thiết kế UI/UX hiện đại (Modern Minimalism) với việc thị giác hóa rủi ro qua mã màu đã đập tan rào cản kỹ thuật, giúp bất kỳ người dùng phổ thông nào cũng có thể dễ dàng tương tác và nắm bắt các phán quyết của AI.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Thứ ba, về mặt Thiết kế Thuật toán Lõi:</b> Lưu đồ thuật toán tuần tự mô tả pipeline <b>PhoBERT Text-only + MLP</b>: embedding 768 chiều → StandardScaler → MLPClassifier (scikit-learn) → verdict 3 mức → ExplanationEngine rule-based.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Tóm lại, những bản thiết kế logic mạch lạc, từ cấp độ Cơ sở dữ liệu (ERD) cho đến sơ đồ Thuật toán lõi được vạch ra trong Chương 3 chính là kim chỉ nam vững chắc. Khung kiến trúc kỹ thuật này đã sẵn sàng để được chuyển hóa thành những dòng mã nguồn thực tế. Toàn bộ quá trình lập trình cài đặt (Implementation) cũng như chạy các thực nghiệm đánh giá hiệu năng mô hình (Evaluation) sẽ được trình bày cặn kẽ trong <b>Chương 4: Hiện thực và Kết quả</b>.</p>
<h1 style="page-break-before: always">CHƯƠNG 4: HIỆN THỰC VÀ
KẾT QUẢ</h1>
<h2>4.1. Môi trường phát triển và Thực nghiệm</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để đảm bảo khả năng hiện thực hóa các bản thiết kế kiến trúc phức tạp ở Chương 3, đặc biệt là việc huấn luyện và chạy suy luận (Inference) cho các mô hình Học Sâu (Deep Learning) đòi hỏi khối lượng tính toán lớn, đồ án đã được triển khai và kiểm thử trên một môi trường máy tính cục bộ (Local Environment) có cấu hình kỹ thuật tiêu chuẩn. Việc thiết lập môi trường được chia thành hai mảng chuyên biệt: Phần cứng và Phần mềm.</p>

<h3>4.1.1. Môi trường Phần cứng (Hardware Environment)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Quá trình huấn luyện mạng nơ-ron đa lớp và kiến trúc Transformer [6, 7] (PhoBERT) đòi hỏi năng lực xử lý ma trận khổng lồ mà các bộ vi xử lý thông thường không thể đáp ứng được trong một thời gian hợp lý. Do đó, hệ thống phần cứng được thiết lập khắt khe với các thông số sau:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Vi xử lý trung tâm (CPU):</b> Tối thiểu Intel Core i5 hoặc AMD Ryzen 5 thế hệ mới, đáp ứng tốt quá trình cào dữ liệu (Web Scraping) đa luồng bằng BeautifulSoup và xử lý tiền dữ liệu văn bản bằng Regex.</li>
  <li style="margin-bottom: 0.05in;"><b>Bộ nhớ trong (RAM):</b> Tối thiểu <b>16GB</b>. Dung lượng này là ranh giới bắt buộc để hệ thống có thể tải đồng thời tập dữ liệu huấn luyện (Dataset) vào bộ nhớ chính, đồng thời duy trì các máy chủ ảo cục bộ (cả FastAPI và Next.js) hoạt động song song mà không bị hiện tượng tràn RAM (Out-of-memory crash).</li>
  <li style="margin-bottom: 0.05in;"><b>Bộ xử lý Đồ họa (GPU):</b> Khuyến nghị card <b>NVIDIA</b> hỗ trợ <b>CUDA</b> để tăng tốc suy luận PhoBERT (embedding). MLP huấn luyện bằng scikit-learn trên CPU; GPU chủ yếu phục vụ trích embedding hàng loạt khi train offline.</li>
</ul>

<h3>4.1.2. Môi trường Hệ điều hành và Phần mềm</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để tạo ra một nền tảng vận hành mượt mà, hạn chế tối đa các xung đột thư viện (Dependency conflicts) thường gặp trong quá trình biên dịch mô hình AI, đồ án đã lựa chọn và chốt cấu hình các công nghệ phần mềm cốt lõi như sau:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Hệ điều hành cốt lõi:</b> <b>Linux (Ubuntu)</b> — tương thích mã nguồn mở, khởi chạy script điều phối (<code>setup.sh</code>, <code>run.sh</code>) ổn định.</li>
  <li style="margin-bottom: 0.05in;"><b>Hệ sinh thái Backend & AI:</b> 
    <ul style="list-style-type: circle; margin-top: 0.05in; margin-bottom: 0.05in;">
      <li style="margin-bottom: 0.05in;"><b>Ngôn ngữ:</b> Sử dụng phiên bản <code>Python 3.10+</code> (toàn bộ mã nguồn chạy bên trong một môi trường ảo Virtual Environment riêng biệt để cách ly hoàn toàn các thư viện).</li>
      <li style="margin-bottom: 0.05in;"><b>Framework máy chủ:</b> <code>FastAPI</code> kết hợp cùng máy chủ ASGI <code>Uvicorn</code> để kích hoạt khả năng xử lý bất đồng bộ (Asynchronous) ở tốc độ cao nhất.</li>
      <li style="margin-bottom: 0.05in;"><b>Thư viện AI Lõi:</b> <code>PyTorch</code> + <code>Transformers</code> (PhoBERT embedding), <code>Scikit-learn</code> (<code>MLPClassifier</code>, <code>StandardScaler</code>, metrics F1/Precision), <code>joblib</code> (lưu artifact).</li>
    </ul>
  </li>
  <li style="margin-bottom: 0.05in;"><b>Hệ sinh thái Frontend:</b> Được xây dựng hoàn toàn trên nền tảng môi trường cục bộ <code>Node.js</code>. Sử dụng ngôn ngữ <code>TypeScript</code> nhằm ép buộc tính an toàn kiểu dữ liệu (Type-safety). Khung thiết kế chính là <code>Next.js 14</code> kết hợp với hệ sinh thái <code>React</code> và bộ thư viện tiện ích <code>Tailwind CSS</code>.</li>
  <li style="margin-bottom: 0.05in;"><b>Hệ quản trị Cơ sở dữ liệu:</b> Để phục vụ mục đích thực nghiệm và phát triển (Development Phase) linh hoạt, đồ án triển khai CSDL <code>SQLite</code> thay vì cài đặt các hệ thống máy chủ cồng kềnh như MySQL hay PostgreSQL. Mọi giao tiếp nhúng với CSDL được thực hiện hoàn toàn gián tiếp và an toàn thông qua thư viện ORM <code>SQLAlchemy</code>.</li>
</ul>
<h2>4.2. Quá trình hiện thực</h2>
<h3>4.2.1. Cài đặt các module lõi của hệ thống (Core Modules Implementation)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mã nguồn của hệ thống được tổ chức khoa học theo nguyên tắc <b>Separation of Concerns (Tách biệt mối quan tâm)</b>. Thay vì nhồi nhét toàn bộ logic vào một khối lệnh nguyên khối khó kiểm soát, đồ án đã phân rã hệ thống thành các module Python độc lập. Lối kiến trúc này giúp mã nguồn dễ bảo trì, dễ kiểm thử (Unit Test) và dễ dàng nâng cấp thuật toán trong tương lai. Các module lõi được cài đặt như sau:</p>

<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Module Thu thập và Tiền xử lý (<code>data_crawler.py</code>, <code>text_utils.py</code>):</b> Khi người dùng nhập URL, <code>data_crawler.py</code> dùng <code>BeautifulSoup</code> + <code>requests</code> trích title/content từ HTML. Văn bản thu được (hoặc nhập trực tiếp) đi qua <code>preprocess_text</code> trong <code>text_utils.py</code>. Helper <code>TextCleaner</code> (HTML/teencode) chỉ dùng trong test, không nằm luồng chính.</li>
  <li style="margin-bottom: 0.05in;"><b>Module Suy luận Phân loại (<code>phobert_inference.py</code>):</b> Tải PhoBERT-base qua <code>Transformers</code> (PyTorch), trích vector [CLS] 768 chiều, chuẩn hóa bằng <code>StandardScaler</code> và suy luận qua <code>MLPClassifier</code> đã lưu (<code>.joblib</code>). <code>predict_proba</code> trả xác suất tin giả; <code>verdict.py</code> quy đổi 3 mức cảnh báo.</li>
  <li style="margin-bottom: 0.05in;"><b>Module Giải thích (<code>explanation_engine.py</code>):</b> Chạy sau phân loại. Quét văn bản gốc (tỷ lệ IN HOA, dấu câu, văn phong giật gân), áp luật rule-based và sinh JSON giải thích tiếng Việt — không tham gia vector đầu vào MLP.</li>
</ul>

<h3>4.2.2. Dữ liệu nghiên cứu và Quy trình Tiền xử lý</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Giới thiệu bộ dữ liệu (Dataset Overview)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để quá trình huấn luyện mạng MLP mang lại độ chính xác cao nhất trong thực tế, đồ án sử dụng bộ dữ liệu tin giả y tế/sức khỏe tiếng Việt trong tệp <code>full_dataset.csv</code> — <b>10.617 bản ghi</b> gốc, <b>10.609 mẫu</b> sau lọc. Dữ liệu được thu thập từ các nguồn báo chí và tập COVID-19 tiếng Việt (VnExpress, daikynguyen, covid19_dataset, …), tập trung chủ đề y tế và sức khỏe tại Việt Nam.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Biện luận lý do lựa chọn bộ dữ liệu quy mô lớn</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Việc quyết định sử dụng bộ dữ liệu đa lĩnh vực này xuất phát từ ba luận điểm mang tính chiến lược:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Tính khái quát hóa cao (Generalization):</b> Khác với các hệ thống chỉ học trên một miền dữ liệu hẹp, việc học trên <b>10.609 mẫu</b> tin y tế/sức khỏe tiếng Việt giúp mô hình nắm bắt ngữ cảnh chuyên ngành và có thể áp dụng kiểm chứng thông tin sức khỏe trên không gian mạng.</li>
  <li style="margin-bottom: 0.05in;"><b>Độ phong phú của thuật ngữ:</b> Ngữ liệu lớn chứa rất nhiều từ vựng đan xen với cấu trúc câu mang tính mồi chài của giới bán hàng giả hoặc câu view giật gân. Đây là một môi trường thử nghiệm vô cùng lý tưởng để ép mô hình PhoBERT [1] phải học được cách phân biệt ngữ cảnh tiếng Việt ở cấp độ phức tạp nhất.</li>
  <li style="margin-bottom: 0.05in;"><b>Sự phù hợp với phương pháp Heuristics:</b> Các tin giả trên không gian mạng thường xuyên lặp lại các hành vi thao túng tâm lý (như viết hoa toàn bộ tựa đề để lôi kéo, dùng hàng loạt dấu chấm than để kích động). Do đó, bộ dữ liệu khổng lồ này chính là "đất diễn" hiệu quả để Động cơ Giải thích Heuristics của đồ án phát huy tối đa sức mạnh.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Quy trình Tiền xử lý Dữ liệu Huấn luyện (Data Preprocessing Workflow)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Trước khi huấn luyện MLP, toàn bộ tập dữ liệu thô trải qua quy trình làm sạch và chia tập:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Làm sạch (<code>dataset_cleaner.py</code>):</b> Loại bỏ bản ghi thiếu nhãn hoặc văn bản rỗng; kết quả <b>10.609 mẫu</b> hợp lệ.</li>
  <li style="margin-bottom: 0.05in;"><b>Tách tập huấn luyện (Train/Test Split):</b> Chia <b>70% huấn luyện — 30% kiểm thử</b> (stratified, <code>random_state=42</code>), tương đương ~<b>3.183 mẫu</b> hold-out.</li>
  <li style="margin-bottom: 0.05in;"><b>Trích embedding &amp; huấn luyện MLP:</b> Mỗi mẫu qua <code>preprocess_text</code> → PhoBERT [CLS] 768-d → <code>StandardScaler.fit</code> trên train → <code>MLPClassifier.fit</code> (128, 64). Artifact lưu <code>.joblib</code>. Không dùng PyTorch DataLoader hay resampling bắt buộc — tập đã cân bằng tương đối.</li>
</ul>
<h3>4.2.3. Tổ chức cấu trúc mã nguồn (Project Directory Structure)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để đảm bảo tính mở rộng, dễ bảo trì và làm việc nhóm hiệu quả, toàn bộ mã nguồn của dự án được tổ chức chặt chẽ theo mô hình phân tách (Decoupled). Dưới đây là sơ đồ cây thư mục (Directory Tree) minh họa cấu trúc các thành phần cốt lõi của hệ thống ShieldAI:</p>

<pre style="white-space: pre-wrap; font-family: monospace; background-color: #f5f5f5; padding: 10px; border: 1px solid #ccc; line-height: 1.5; overflow-x: auto;"><code>ShieldAI_Project/
├── backend/                  # Khối Máy chủ API (Python &amp; FastAPI)
│   ├── api/                  # Khai báo các API Endpoints (Auth, Analyze, History)
│   ├── auth/                 # Xử lý bảo mật, mã hóa JWT, phân quyền
│   ├── database/             # Kết nối CSDL SQLite và quản lý Models (SQLAlchemy)
│   ├── experiments/          # Lưu trữ kết quả thực nghiệm, biểu đồ đánh giá mô hình
│   ├── models/               # Artifact MLP + StandardScaler (.joblib); cache PhoBERT
│   ├── tests/                # Bộ kịch bản kiểm thử tự động (Pytest) [14]
│   ├── training/             # Chứa Jupyter Notebook để huấn luyện mô hình (train_phobert_model.ipynb)
│   ├── data_crawler.py       # Module cào dữ liệu thô từ Internet
│   ├── dataset_cleaner.py    # Module tiền xử lý và làm sạch dữ liệu thô
│   ├── explanation_engine.py # Động cơ Giải thích: Bóc tách và định lượng nguyên nhân lừa đảo
│   ├── text_utils.py         # preprocess_text, PyVi; helper TextCleaner (test)
│   ├── phobert_inference.py  # PhoBERT embedding + joblib MLP + verdict
│   └── main.py               # Điểm khởi chạy (Entry point) của máy chủ FastAPI
├── docs/                     # Tài liệu kỹ thuật, Hướng dẫn cài đặt và Nhật ký dự án
├── frontend/                 # Khối Giao diện Người dùng (TypeScript &amp; Next.js)
│   ├── app/                  # Kiến trúc App Router của Next.js (chứa các trang /login, /analyze,...)
│   ├── components/           # Các Component tái sử dụng (Navbar, Chart, HeroBanner)
│   ├── context/              # Quản lý trạng thái toàn cục (React Context API cho Auth)
│   ├── lib/                  # Các hàm tiện ích (gọi API, xử lý hiệu ứng Motion)
│   └── tailwind.config.ts    # Cấu hình hệ thống thiết kế (Design System &amp; Colors)
├── scripts/                  # setup.sh, run.sh (all | api | web | test)
├── setup.sh / run.sh         # Wrapper gọc scripts/
├── README.md                 # Tài liệu tổng quan giới thiệu dự án
└── requirements.txt          # Danh sách các thư viện Python phụ thuộc</code></pre>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mô hình tổ chức này tuân thủ nguyên tắc <i>Separation of Concerns</i> (Tách biệt mối quan tâm), giúp đội ngũ phát triển dễ dàng khoanh vùng lỗi, thực hiện kiểm thử độc lập ở Backend mà không ảnh hưởng tới quá trình thiết kế UI/UX ở Frontend.</p>

<h2>4.3. Kết quả đạt được</h2>
<h3>4.3.1. Kết quả giao diện ứng dụng (User Interface Implementation)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Hệ thống đã được lập trình hoàn thiện bằng Next.js và triển khai thành công trên môi trường cục bộ. Giao diện thực tế hoạt động trơn tru, đáp ứng chính xác các yêu cầu về thiết kế UI/UX (Modern Minimalism) đã đề ra ở Chương 3. Dưới đây là các minh chứng hình ảnh chụp lại từ hệ thống thực tế đang vận hành:</p>

<p align="center" style="margin-top: 0.2in;">
  <img src="image/1_TrangChu.png" alt="Giao diện Trang Chủ ShieldAI" width="100%" style="border: 1px solid #ccc; border-radius: 8px;">
  <br><i style="font-size: 0.9em; color: #555;">Hình 4.1. Giao diện màn hình Cổng thông tin (Home) với thiết kế tối giản, tông màu tối chuyên nghiệp.</i>
</p>

<p align="center" style="margin-top: 0.2in;">
  <img src="image/2_TrangDangNhap.png" alt="Giao diện Đăng nhập" width="100%" style="border: 1px solid #ccc; border-radius: 8px;">
  <br><i style="font-size: 0.9em; color: #555;">Hình 4.2. Giao diện Đăng nhập (Authentication) bảo mật người dùng.</i>
</p>

<p align="center" style="margin-top: 0.2in;">
  <img src="image/4_TrangPhanTich_TabVanBan.png" alt="Giao diện Phân tích văn bản" width="100%" style="border: 1px solid #ccc; border-radius: 8px;">
  <br><i style="font-size: 0.9em; color: #555;">Hình 4.3. Giao diện trung tâm Phân tích — nhập văn bản thô hoặc URL để kiểm chứng.</i>
</p>

<p align="center" style="margin-top: 0.2in;">
  <img src="image/6_KetQua_TinGia_TongQuan.png" alt="Kết quả phát hiện Tin Giả" width="100%" style="border: 1px solid #ccc; border-radius: 8px;">
  <br><i style="font-size: 0.9em; color: #555;">Hình 4.4. Báo cáo phân tích cảnh báo nguy cơ Tin Giả thông qua nguyên lý Thị giác hóa rủi ro (Màu Đỏ).</i>
</p>

<p align="center" style="margin-top: 0.2in;">
  <img src="image/10_KetQua_TinThat.png" alt="Kết quả xác thực Tin Thật" width="100%" style="border: 1px solid #ccc; border-radius: 8px;">
  <br><i style="font-size: 0.9em; color: #555;">Hình 4.5. Báo cáo phân tích xác thực Tin Thật an toàn (Màu Xanh lá cây).</i>
</p>

<p align="center" style="margin-top: 0.2in;">
  <img src="image/7_KetQua_TinGia_GiaiThichXAI.png" alt="Báo cáo giải thích Giải thích Heuristic" width="100%" style="border: 1px solid #ccc; border-radius: 8px;">
  <br><i style="font-size: 0.9em; color: #555;">Hình 4.6. Trình diễn khả năng của Động cơ Giải thích: Hệ thống bóc tách rõ lý do bài báo bị đánh dấu lừa đảo (Giọng điệu kích động, lạm dụng dấu chấm than).</i>
</p>

<p align="center" style="margin-top: 0.2in;">
  <img src="image/9_TrangLichSu.png" alt="Quản lý Lịch sử" width="100%" style="border: 1px solid #ccc; border-radius: 8px;">
  <br><i style="font-size: 0.9em; color: #555;">Hình 4.7. Màn hình Quản lý Lịch sử cá nhân với thiết kế dạng danh sách thẻ động (Dynamic Cards).</i>
</p>

<h3>4.3.2. Đánh giá kết quả bằng số liệu thực nghiệm</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để minh chứng tính đúng đắn của phương pháp tiếp cận, đồ án không chỉ dựa vào đánh giá cảm quan trên giao diện mà còn tiến hành định lượng (Quantitative Evaluation) hệ thống bằng các độ đo học máy chuẩn mực. Thử nghiệm được tiến hành trên tập kiểm thử hold-out <b>30%</b> (~3.183 mẫu) chưa từng được mô hình nhìn thấy trong quá trình huấn luyện.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>a) Các độ đo đánh giá (Evaluation Metrics)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Hệ thống sử dụng ma trận nhầm lẫn (Confusion Matrix) để tính toán 4 chỉ số cốt lõi:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Accuracy (Độ chính xác tổng thể):</b> Tỷ lệ phần trăm các bài báo (cả thật và giả) được hệ thống phân loại đúng. Tuy nhiên, trong bài toán tin giả, chỉ số này không phản ánh toàn diện bức tranh nếu dữ liệu bị mất cân bằng.</li>
  <li style="margin-bottom: 0.05in;"><b>Precision (Độ chuẩn xác):</b> Trong số những bài báo bị hệ thống gắn cờ "Tin Giả", có bao nhiêu bài thực sự là giả. Độ đo này cực kỳ quan trọng để hạn chế hiện tượng <i>Dương tính giả (False Positive)</i>, tức là đánh oan một bài báo chính thống.</li>
  <li style="margin-bottom: 0.05in;"><b>Recall (Độ bao phủ):</b> Trong tổng số các bài Tin Giả đang tồn tại trong thực tế, hệ thống "tóm" được bao nhiêu phần trăm. Độ đo này giúp đánh giá khả năng không bỏ lọt tội phạm <i>(Âm tính giả - False Negative)</i>.</li>
  <li style="margin-bottom: 0.05in;"><b>F1-Score:</b> Trung bình điều hòa (Harmonic Mean) giữa Precision và Recall. Đây là "thước đo vàng" (Gold Standard) để đánh giá năng lực thực sự của một hệ thống phát hiện tin giả.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>b) Kết quả so sánh trên tập kiểm thử</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để đảm bảo tính khách quan trong việc đánh giá hiệu năng, toàn bộ <b>10.609 mẫu</b> sau lọc đã được chia tách theo tỷ lệ <b>70% (Huấn luyện) — 30% (Kiểm thử)</b>, tương đương khoảng <b>~3.183 mẫu</b> tập kiểm thử hold-out. Quá trình chia tách sử dụng phương pháp phân tầng (Stratified Split) với <code>random_state=42</code> để đảm bảo phân phối nhãn (Thật/Giả) đồng đều, ngăn chặn hiện tượng rò rỉ dữ liệu (Data Leakage). Quá trình huấn luyện còn được củng cố bởi phương pháp kiểm định chéo 5-Fold Cross Validation.</p>

Đồ án đã tiến hành đánh giá chi tiết hiệu năng của mô hình <b>PhoBERT Text-only + MLP (Hệ thống ShieldAI)</b> trên tập kiểm thử hoàn toàn độc lập (chiếm 30% dữ liệu). Kết quả được trình bày chi tiết trong Bảng 4.1:</p>

<p align="center" style="margin-top: 0.2in; font-style: italic; margin-bottom: 0.05in;">Bảng 4.1. Hiệu năng của mô hình PhoBERT Text-only + MLP</p>
<table width="100%" border="1" cellpadding="8" cellspacing="0" style="display: table; width: 100%; border-collapse: collapse; border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; table-layout: fixed;">
  <tr style="background-color: #f2f2f2; text-align: center; font-weight: bold;">
    <td width="28%" style="border: 1px solid #000;">Mô hình (Model)</td>
    <td width="18%" style="border: 1px solid #000;">Accuracy</td>
    <td width="18%" style="border: 1px solid #000;">F1-Score</td>
    <td width="18%" style="border: 1px solid #000;">ROC-AUC</td>
    <td width="18%" style="border: 1px solid #000;">5-Fold CV (F1)</td>
  </tr>
  <tr style="text-align: center; background-color: #e6f7ff;">
    <td style="border: 1px solid #000; text-align: left;"><b>PhoBERT Text-only + MLP</b></td>
    <td style="border: 1px solid #000;"><b>94.13%</b></td>
    <td style="border: 1px solid #000; color: red;"><b>93.71%</b></td>
    <td style="border: 1px solid #000;"><b>98.50%</b></td>
    <td style="border: 1px solid #000;"><b>93.17% ± 1.33%</b></td>
  </tr>
</table>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Từ Bảng 4.1, có thể thấy kiến trúc tinh gọn của hệ thống đã đạt được các chỉ số thực nghiệm vô cùng ấn tượng. Việc loại bỏ các vector Heuristics phức tạp không những không làm suy giảm sức mạnh của PhoBERT, mà còn giúp mô hình học sâu tập trung hoàn toàn vào khả năng phân tích ngữ nghĩa, đạt được F1-Score lên tới 93,71% trên tập kiểm thử hold-out (~3.183 mẫu, 30% của 10.609 mẫu).</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>c) Phân tích sự ổn định qua Kiểm định chéo (Cross-validation)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để tăng cường sức thuyết phục khoa học, đồ án đã áp dụng phương pháp <b>Kiểm định chéo 5 phần (5-Fold Cross Validation)</b>. Kết quả đạt <b>F1: 93.17% ± 1.33%</b> chứng minh rằng hiệu năng của hệ thống không phụ thuộc vào sự may mắn ngẫu nhiên khi chia tách dữ liệu, mà luôn ổn định một cách vững chắc. Đặc biệt, chỉ số <b>ROC-AUC đạt 98.50%</b> khẳng định khả năng phân tách tuyệt vời giữa hai lớp Thật và Giả của mạng Nơ-ron đa tầng MLP.</p>
<h2>4.4. Kiểm thử hệ thống (System Testing)</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để đảm bảo độ tin cậy và tính bền vững của phần mềm trước khi nghiệm thu, đồ án đã triển khai một quy trình kiểm thử cơ bản, tập trung vào các kịch bản trọng yếu thông qua kiểm thử tự động (Automated Testing) và kiểm thử thủ công (Black-box Testing).</p>

<h3>4.4.1. Kiểm thử tự động bằng Pytest (Automated Testing)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Hệ thống Backend được tích hợp bộ kiểm thử <code>pytest</code> trong thư mục <code>backend/tests/</code>. Tổng cộng <b>42 kịch bản (test cases)</b> chạy tự động, gồm kiểm thử đơn vị (unit test) và kiểm thử tích hợp API (integration test). Các test API dùng SQLite in-memory và mock <code>PhoBERTInferenceSystem</code>; lỗi nghiệp vụ (auth, input trống) được assert qua <code>status=error</code> trong body JSON với HTTP 200.</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Cách chạy:</b> <code>./run.sh test</code> hoặc <code>cd backend &amp;&amp; ./run_tests.sh</code>. Kết quả hiện tại: <b>42/42 PASSED</b> (~4 giây).</p>

<p align="center" style="margin-top: 0.2in; font-style: italic; margin-bottom: 0.05in;">Bảng 4.3. Bộ kiểm thử tự động Pytest (backend/tests/)</p>
<table width="100%" border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; border: 1px solid #000; font-size: 0.95em;">
  <tr style="background-color: #f2f2f2; font-weight: bold;">
    <td style="border: 1px solid #000; text-align: center;">STT</td>
    <td style="border: 1px solid #000;">File test</td>
    <td style="border: 1px solid #000; text-align: center;">Số TC</td>
    <td style="border: 1px solid #000;">Phạm vi kiểm thử</td>
    <td style="border: 1px solid #000;">Kỹ thuật / Kỳ vọng</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">1</td>
    <td style="border: 1px solid #000;"><code>test_verdict.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">5</td>
    <td style="border: 1px solid #000;">Phân loại 3 mức từ xác suất</td>
    <td style="border: 1px solid #000;">Ngưỡng ≥75% tin giả, 35–74% đáng ngờ, &lt;35% tin thật; kiểm tra biên 75/74.9/35/34.9</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">2</td>
    <td style="border: 1px solid #000;"><code>test_text_utils.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">5</td>
    <td style="border: 1px solid #000;">Pipeline <code>preprocess_text</code></td>
    <td style="border: 1px solid #000;">Xóa URL, lowercase, PyVi; thống nhất train/inference/dataset_cleaner</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">3</td>
    <td style="border: 1px solid #000;"><code>test_text_cleaner.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">3</td>
    <td style="border: 1px solid #000;">Helper <code>TextCleaner</code> (không luồng inference chính)</td>
    <td style="border: 1px solid #000;">HTML/teencode; TC-09 đối chiếu với <code>preprocess_text</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">4</td>
    <td style="border: 1px solid #000;"><code>test_explanation_engine.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">6</td>
    <td style="border: 1px solid #000;">Động cơ giải thích XAI</td>
    <td style="border: 1px solid #000;">Ngưỡng model note khớp verdict; phát hiện văn phong giật gân; <code>build_explanation</code> JSON</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">5</td>
    <td style="border: 1px solid #000;"><code>test_dataset_cleaner.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">3</td>
    <td style="border: 1px solid #000;">Lọc CSV trước train</td>
    <td style="border: 1px solid #000;">Bỏ thiếu content, &lt;5 từ, trùng lặp; tạo cột <code>content_segmented</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">6</td>
    <td style="border: 1px solid #000;"><code>test_data_crawler.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">3</td>
    <td style="border: 1px solid #000;">Thu thập văn bản / URL</td>
    <td style="border: 1px solid #000;">Nhập text thủ công; mock HTTP crawl HTML → parse h1/p</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">7</td>
    <td style="border: 1px solid #000;"><code>test_phobert_inference.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">4</td>
    <td style="border: 1px solid #000;">Pipeline suy luận 3 mô-đun</td>
    <td style="border: 1px solid #000;">Mock PhoBERT/MLP: thiếu model, từ chối &lt;5 từ, phân loại fake, luồng <code>infer()</code> đầy đủ</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">8</td>
    <td style="border: 1px solid #000;"><code>test_history_service.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">1</td>
    <td style="border: 1px solid #000;">Lưu trữ SQLite</td>
    <td style="border: 1px solid #000;"><code>save_analysis</code> + <code>list_user_history</code> trả đúng verdict/prob</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">9</td>
    <td style="border: 1px solid #000;"><code>test_auth_api.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">4</td>
    <td style="border: 1px solid #000;">API xác thực JWT</td>
    <td style="border: 1px solid #000;">Đăng ký/đăng nhập/<code>/me</code>; email trùng; sai mật khẩu</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; text-align: center;">10</td>
    <td style="border: 1px solid #000;"><code>test_api.py</code></td>
    <td style="border: 1px solid #000; text-align: center;">8</td>
    <td style="border: 1px solid #000;">API phân tích &amp; lịch sử</td>
    <td style="border: 1px solid #000;">Health, analyze (text/url), lịch sử CRUD, cô lập dữ liệu giữa 2 user</td>
  </tr>
  <tr style="background-color: #f9f9f9; font-weight: bold;">
    <td style="border: 1px solid #000; text-align: center;" colspan="2">Tổng cộng</td>
    <td style="border: 1px solid #000; text-align: center;">42</td>
    <td style="border: 1px solid #000;" colspan="2">Unit: 30 | API integration: 12 | Fixture: <code>conftest.py</code> (DB test + mock inference)</td>
  </tr>
</table>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Bảng 4.3 tổng hợp theo file test. Dưới đây, <b>42 kịch bản</b> được phân thành <b>8 nhóm chức năng</b> và liệt kê chi tiết tại Bảng 4.4 (ánh xạ FR từ Bảng 3.1):</p>

<ul style="line-height: 150%; margin-left: 0.5in; margin-bottom: 0.1in;">
  <li><b>Nhóm 1 — Verdict 3 mức</b> (TC-01 → TC-05, <code>test_verdict.py</code>): kiểm tra ngưỡng 75% / 35% và giá trị biên.</li>
  <li><b>Nhóm 2 — Tiền xử lý văn bản</b> (TC-06 → TC-13): <code>preprocess_text</code> (TC-06–08, TC-10); helper <code>TextCleaner</code> (TC-09, TC-11–13, không nằm luồng inference chính).</li>
  <li><b>Nhóm 3 — Giải thích XAI</b> (TC-14 → TC-19, <code>test_explanation_engine.py</code>): ngưỡng giải thích khớp <code>verdict.py</code>, phát hiện giật gân.</li>
  <li><b>Nhóm 4 — Dữ liệu &amp; Crawl</b> (TC-20 → TC-25): lọc CSV, nhập text, crawl HTML mock.</li>
  <li><b>Nhóm 5 — Pipeline suy luận</b> (TC-26 → TC-29, <code>test_phobert_inference.py</code>): 3 mô-đun + luồng <code>infer()</code> (mock PhoBERT).</li>
  <li><b>Nhóm 6 — Lịch sử SQLite</b> (TC-30, <code>test_history_service.py</code>): lưu và đọc kết quả phân tích.</li>
  <li><b>Nhóm 7 — API xác thực</b> (TC-31 → TC-34, <code>test_auth_api.py</code>): đăng ký, đăng nhập, JWT.</li>
  <li><b>Nhóm 8 — API phân tích &amp; lịch sử</b> (TC-35 → TC-42, <code>test_api.py</code>): health, analyze, CRUD history, cô lập user.</li>
</ul>

<h4>4.4.1.1. Phân nhóm và chi tiết 42 test cases</h4>

<p align="center" style="margin-top: 0.2in; font-style: italic; margin-bottom: 0.05in;">Bảng 4.4. Chi tiết từng kịch bản kiểm thử tự động (42 test cases)</p>
<table width="100%" border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; border: 1px solid #000; font-size: 0.85em;">
  <tr style="background-color: #f2f2f2; font-weight: bold;">
    <td style="border: 1px solid #000; text-align: center; width: 5%;">Mã</td>
    <td style="border: 1px solid #000; width: 20%;">Hàm test</td>
    <td style="border: 1px solid #000; text-align: center; width: 6%;">Loại</td>
    <td style="border: 1px solid #000; text-align: center; width: 7%;">FR</td>
    <td style="border: 1px solid #000; width: 28%;">Đầu vào / Kịch bản</td>
    <td style="border: 1px solid #000; width: 34%;">Kỳ vọng (kết quả assert)</td>
  </tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-01</td><td style="border: 1px solid #000;"><code>test_verdict_thresholds[80]</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-05</td><td style="border: 1px solid #000;">Xác suất tin giả = 80%</td><td style="border: 1px solid #000;"><code>verdict=fake</code>, nhãn <code>TIN GIẢ (FAKE)</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-02</td><td style="border: 1px solid #000;"><code>test_verdict_thresholds[60]</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-05</td><td style="border: 1px solid #000;">Xác suất tin giả = 60%</td><td style="border: 1px solid #000;"><code>verdict=suspicious</code>, nhãn <code>ĐÁNG NGỜ</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-03</td><td style="border: 1px solid #000;"><code>test_verdict_thresholds[45]</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-05</td><td style="border: 1px solid #000;">Xác suất tin giả = 45%</td><td style="border: 1px solid #000;"><code>verdict=suspicious</code>, nhãn <code>ĐÁNG NGỜ</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-04</td><td style="border: 1px solid #000;"><code>test_verdict_thresholds[30]</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-05</td><td style="border: 1px solid #000;">Xác suất tin giả = 30%</td><td style="border: 1px solid #000;"><code>verdict=real</code>, nhãn <code>TIN THẬT (REAL)</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-05</td><td style="border: 1px solid #000;"><code>test_verdict_boundary_values</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-05</td><td style="border: 1px solid #000;">Biên ngưỡng: 75, 74.9, 35, 34.9</td><td style="border: 1px solid #000;">75→fake; 74.9→suspicious; 35→suspicious; 34.9→real</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-06</td><td style="border: 1px solid #000;"><code>test_preprocess_text_basic</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-03</td><td style="border: 1px solid #000;">Văn bản chứa URL <code>https://example.com</code></td><td style="border: 1px solid #000;">Không còn <code>http</code>/<code>example.com</code>; có token PyVi (<code>_</code>)</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-07</td><td style="border: 1px solid #000;"><code>test_segment_for_training_matches_preprocess_text</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-03</td><td style="border: 1px solid #000;">Câu y tế mẫu</td><td style="border: 1px solid #000;"><code>segment_for_training()</code> == <code>preprocess_text()</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-08</td><td style="border: 1px solid #000;"><code>test_dataset_cleaner_uses_same_pipeline</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-03</td><td style="border: 1px solid #000;">Text giật gân + URL</td><td style="border: 1px solid #000;"><code>segment_text()</code> == <code>preprocess_text()</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-09</td><td style="border: 1px solid #000;"><code>test_text_cleaner_pipeline_matches_preprocess_text</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">Helper <code>TextCleaner</code> vs <code>preprocess_text</code></td><td style="border: 1px solid #000;"><code>pipeline_clean()</code> == <code>preprocess_text()</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-10</td><td style="border: 1px solid #000;"><code>test_preprocess_text_empty</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-03</td><td style="border: 1px solid #000;">Chuỗi rỗng <code>""</code> và <code>None</code></td><td style="border: 1px solid #000;">Trả về <code>""</code>, không lỗi</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-11</td><td style="border: 1px solid #000;"><code>test_remove_html_and_urls</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">Helper: thẻ <code>&lt;a href&gt;</code> + URL</td><td style="border: 1px solid #000;">Xóa HTML/URL; giữ <code>vào đây</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-12</td><td style="border: 1px solid #000;"><code>test_normalize_teencode</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">Helper: teencode <code>wa</code>, <code>j</code>, <code>ng</code></td><td style="border: 1px solid #000;">→ <code>quá</code>, <code>gì</code>, <code>người</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-13</td><td style="border: 1px solid #000;"><code>test_pipeline_clean</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">Helper <code>TextCleaner.pipeline_clean</code></td><td style="border: 1px solid #000;">Lowercase, không URL, có PyVi</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-14</td><td style="border: 1px solid #000;"><code>test_phobert_summary_aligns_with_verdict_thresholds</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-06</td><td style="border: 1px solid #000;">Xác suất 80% / 50% / 20%</td><td style="border: 1px solid #000;">Tóm tắt chứa <code>tin giả</code> / <code>đối chiếu</code> / <code>chính thống</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-15</td><td style="border: 1px solid #000;"><code>test_phobert_summary_boundary_at_fake_threshold</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-06</td><td style="border: 1px solid #000;">Biên ngưỡng fake: 75% và 74.9%</td><td style="border: 1px solid #000;">75%→<code>tin giả</code>; 74.9%→<code>đối chiếu</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-16</td><td style="border: 1px solid #000;"><code>test_phobert_summary_boundary_at_suspicious_threshold</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-06</td><td style="border: 1px solid #000;">Biên ngưỡng suspicious: 35% và 34.9%</td><td style="border: 1px solid #000;">35%→<code>đối chiếu</code>; 34.9%→<code>chính thống</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-17</td><td style="border: 1px solid #000;"><code>test_scan_text_signals_detects_sensational_language</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-06</td><td style="border: 1px solid #000;">Tiêu đề + nội dung giật gân (<code>CẢNH BÁO KHẨN CẤP</code>)</td><td style="border: 1px solid #000;">Signal có <code>type=text_risk</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-18</td><td style="border: 1px solid #000;"><code>test_build_explanation_matches_verdict_for_fake</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-06</td><td style="border: 1px solid #000;"><code>fake_prob=85</code>, nội dung giật gân</td><td style="border: 1px solid #000;"><code>verdict=fake</code>, headline chứa <code>TIN GIẢ</code>, ≥1 lý do</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-19</td><td style="border: 1px solid #000;"><code>test_build_explanation_real_news_tone</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-06</td><td style="border: 1px solid #000;"><code>fake_prob=10</code>, văn phong báo chí khách quan</td><td style="border: 1px solid #000;"><code>verdict=real</code>, headline chứa <code>TIN THẬT</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-20</td><td style="border: 1px solid #000;"><code>test_filter_dataset_removes_short_missing_and_duplicates</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">DataFrame 5 dòng: ngắn, thiếu, trùng</td><td style="border: 1px solid #000;">Còn 2 dòng hợp lệ; <code>content</code> unique</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-21</td><td style="border: 1px solid #000;"><code>test_fill_missing_text_columns</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">DataFrame có <code>content=None</code></td><td style="border: 1px solid #000;"><code>title</code> không còn NA</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-22</td><td style="border: 1px solid #000;"><code>test_add_segmented_column_creates_pyvi_tokens</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-03</td><td style="border: 1px solid #000;">DataFrame sau <code>filter_dataset</code></td><td style="border: 1px solid #000;">Có cột <code>content_segmented</code>, không rỗng</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-23</td><td style="border: 1px solid #000;"><code>test_get_article_from_text_success</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-01</td><td style="border: 1px solid #000;">Nhập text + tiêu đề thủ công</td><td style="border: 1px solid #000;"><code>status=success</code>, <code>source_domain=user_input</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-24</td><td style="border: 1px solid #000;"><code>test_get_article_from_text_empty</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-01</td><td style="border: 1px solid #000;">Chuỗi chỉ khoảng trắng <code>"   "</code></td><td style="border: 1px solid #000;"><code>status=error</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-25</td><td style="border: 1px solid #000;"><code>test_crawl_news_article_parses_html</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-02</td><td style="border: 1px solid #000;">Mock HTTP HTML có <code>&lt;h1&gt;</code> và <code>&lt;p&gt;</code></td><td style="border: 1px solid #000;">Parse title, content; <code>source_domain=vnexpress.net</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-26</td><td style="border: 1px solid #000;"><code>test_infer_fails_when_model_not_loaded</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;"><code>model_loaded=False</code></td><td style="border: 1px solid #000;"><code>status=error</code>, message gợi ý train model</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-27</td><td style="border: 1px solid #000;"><code>test_module_1_rejects_short_content</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-03</td><td style="border: 1px solid #000;">Nội dung chỉ 3 từ</td><td style="border: 1px solid #000;"><code>clean=None</code>, <code>raw.status=error</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-28</td><td style="border: 1px solid #000;"><code>test_module_3_classification_fake_verdict</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-05</td><td style="border: 1px solid #000;">Mock MLP trả xác suất 82%</td><td style="border: 1px solid #000;"><code>verdict=fake</code>, <code>fake_prob≈82</code>, nhãn chứa <code>FAKE</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-29</td><td style="border: 1px solid #000;"><code>test_infer_success_pipeline</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-04,05</td><td style="border: 1px solid #000;">Mock module 1→2→3 + explanation</td><td style="border: 1px solid #000;"><code>status=success</code>; gọi đủ 4 bước pipeline</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-30</td><td style="border: 1px solid #000;"><code>test_save_and_list_analysis</code></td><td style="border: 1px solid #000; text-align: center;">Unit</td><td style="border: 1px solid #000; text-align: center;">FR-07</td><td style="border: 1px solid #000;">Lưu kết quả phân tích vào SQLite test</td><td style="border: 1px solid #000;"><code>total=1</code>, <code>verdict=suspicious</code>, <code>fake_prob=42.5</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-31</td><td style="border: 1px solid #000;"><code>test_register_and_login_flow</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">POST register → login → GET <code>/api/auth/me</code></td><td style="border: 1px solid #000;">Có JWT token; email khớp ở cả 3 bước</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-32</td><td style="border: 1px solid #000;"><code>test_register_duplicate_email</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">Đăng ký 2 lần cùng email</td><td style="border: 1px solid #000;">Lần 2: <code>status=error</code>, message chứa <code>Email</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-33</td><td style="border: 1px solid #000;"><code>test_login_wrong_password</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">Đăng nhập sai mật khẩu</td><td style="border: 1px solid #000;"><code>status=error</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-34</td><td style="border: 1px solid #000;"><code>test_me_requires_auth</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">—</td><td style="border: 1px solid #000;">GET <code>/api/auth/me</code> không có JWT</td><td style="border: 1px solid #000;"><code>status=error</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-35</td><td style="border: 1px solid #000;"><code>test_health_check</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">FR-08</td><td style="border: 1px solid #000;">GET <code>/api/health</code></td><td style="border: 1px solid #000;"><code>status=ok</code>, <code>model_loaded=true</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-36</td><td style="border: 1px solid #000;"><code>test_analyze_unauthorized</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">FR-08</td><td style="border: 1px solid #000;">POST <code>/api/analyze</code> không JWT</td><td style="border: 1px solid #000;"><code>status=error</code>, yêu cầu đăng nhập</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-37</td><td style="border: 1px solid #000;"><code>test_analyze_empty_text_when_authenticated</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">FR-01</td><td style="border: 1px solid #000;">JWT hợp lệ, <code>text=""</code></td><td style="border: 1px solid #000;"><code>status=error</code>, message chứa <code>trống</code></td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-38</td><td style="border: 1px solid #000;"><code>test_analyze_text_success</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">FR-01,05,06,07</td><td style="border: 1px solid #000;">JWT + text giật gân đủ dài</td><td style="border: 1px solid #000;"><code>status=success</code>; có verdict, fake_prob, explanation, history_id</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-39</td><td style="border: 1px solid #000;"><code>test_analyze_url_mode</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">FR-02,05</td><td style="border: 1px solid #000;"><code>mode=url</code> + link VnExpress</td><td style="border: 1px solid #000;"><code>status=success</code>; <code>infer(url=...)</code> được gọi</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-40</td><td style="border: 1px solid #000;"><code>test_history_list_after_analyze</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">FR-07</td><td style="border: 1px solid #000;">Analyze xong → GET <code>/api/history</code></td><td style="border: 1px solid #000;"><code>total≥1</code>, có ít nhất 1 item</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-41</td><td style="border: 1px solid #000;"><code>test_history_detail_and_delete</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">FR-07</td><td style="border: 1px solid #000;">GET detail → DELETE → GET lại</td><td style="border: 1px solid #000;">Detail OK; delete OK; lần GET sau báo error</td></tr>
  <tr><td style="border: 1px solid #000; text-align: center;">TC-42</td><td style="border: 1px solid #000;"><code>test_history_isolated_between_users</code></td><td style="border: 1px solid #000; text-align: center;">API</td><td style="border: 1px solid #000; text-align: center;">FR-07,08</td><td style="border: 1px solid #000;">User A tạo history; User B truy cập</td><td style="border: 1px solid #000;">User B nhận <code>status=error</code> (cô lập dữ liệu)</td></tr>
</table>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><i>Ghi chú cột FR:</i> ánh xạ Bảng 3.1; <code>—</code> = kiểm thử helper (<code>TextCleaner</code>), auth nội bộ, hoặc pipeline dữ liệu. API lỗi nghiệp vụ: HTTP <b>200</b> + <code>status=error</code> + <code>message</code> (TC-32–34, TC-36–37, …).</p>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Đánh giá:</b> 100% (42/42) test cases đạt PASSED. Kiểm thử API dùng mock inference nên không phụ thuộc GPU/RAM PhoBERT; DB test tách biệt file <code>shieldai.db</code> production.</p>

<h3>4.4.2. Kiểm thử Hộp đen mức Ứng dụng (Manual Black-box Testing)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Ở tầng giao diện trực quan (Frontend), đồ án tiến hành kiểm thử các luồng thao tác thực tế nhằm đảm bảo trải nghiệm nghiệp vụ xuyên suốt, không bị đứt gãy. Bảng 4.2 dưới đây mô tả các kịch bản tiêu biểu:</p>

<p align="center" style="margin-top: 0.2in; font-style: italic; margin-bottom: 0.05in;">Bảng 4.2. Danh sách Kịch bản Kiểm thử Hộp đen</p>
<table width="100%" border="1" cellpadding="8" cellspacing="0" style="display: table; width: 100%; border-collapse: collapse; border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; table-layout: fixed; word-wrap: break-word; word-break: break-word; white-space: normal;">
  <tr style="background-color: #f2f2f2; font-weight: bold;">
    <td width="8%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center;">ID</td>
    <td width="30%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Kịch bản (Test Scenario)</td>
    <td width="30%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Kết quả mong đợi (Expected)</td>
    <td width="22%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Kết quả thực tế</td>
    <td width="10%" style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center;">Status</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center;">TC_01</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Nhập URL một bài báo chính thống hợp lệ từ báo điện tử VnExpress.</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hệ thống cào thành công tiêu đề, nội dung bài báo và hiển thị kết quả phân tích ổn định.</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Cào đúng nội dung cốt lõi, tự động loại bỏ các đoạn quảng cáo (Ads).</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; color: green; font-weight: bold; text-align: center;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center;">TC_02</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Nhập URL bị lỗi (404) hoặc nhập một trang web không phải trang tin tức (Ví dụ: Facebook cá nhân).</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hệ thống tự động báo lỗi "Không thể trích xuất nội dung" và chặn lệnh gửi phân tích cho AI.</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Hiển thị thông báo Toast Notification rõ ràng trên giao diện người dùng.</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; color: green; font-weight: bold; text-align: center;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; text-align: center;">TC_03</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Gửi phân tích một đoạn văn bản lừa đảo (cố tình lạm dụng viết hoa toàn bộ và dùng hàng loạt dấu chấm than !!!).</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Cảnh báo đỏ (Tin giả). Động cơ Giải thích phải vạch trần được thủ thuật hình thức này.</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word;">Thanh đánh giá báo động đỏ phần "Thống kê hình thức".</td>
    <td style="border: 1px solid #000; white-space: normal; word-wrap: break-word; word-break: break-word; color: green; font-weight: bold; text-align: center;">PASS</td>
  </tr>
</table>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Dưới đây là một số hình ảnh thực tế minh họa cho các kịch bản kiểm thử hộp đen đã được thực thi và xác nhận trên môi trường Frontend:</p>

<div align="center" style="margin-top: 20px; margin-bottom: 20px;">
  <p style="font-style: italic; margin-bottom: 10px;">Hình 4.8. Minh họa Kịch bản TC_01: Phân tích bài báo chính thống (0% Tin giả)</p>
  <img src="image/11_TC01_NhapURL_VnExpress.png" alt="Nhập URL VnExpress" width="90%" style="border: 1px solid #ddd; border-radius: 5px; margin-bottom: 10px;">
  <br>
  <img src="image/12_TC01_KetQua_TinThat.png" alt="Kết quả Tin Thật" width="90%" style="border: 1px solid #ddd; border-radius: 5px; margin-bottom: 10px;">
  <br>
  <img src="image/13_TC01_GiaiThichXAI_TinThat.png" alt="Giải thích Dữ liệu" width="90%" style="border: 1px solid #ddd; border-radius: 5px;">
</div>

<div align="center" style="margin-top: 20px; margin-bottom: 20px;">
  <p style="font-style: italic; margin-bottom: 10px;">Hình 4.11. Minh họa Kịch bản TC_02: Ngăn chặn lỗi khi phân tích URL sai định dạng</p>
  <img src="image/15_TC02_BaoLoiURL_KhongHopLe.png" alt="Báo lỗi URL" width="90%" style="border: 1px solid #ddd; border-radius: 5px;">
</div>

<div align="center" style="margin-top: 20px; margin-bottom: 20px;">
  <p style="font-style: italic; margin-bottom: 10px;">Hình 4.12. Minh họa Kịch bản TC_03: Bóc trần thủ thuật lạm dụng hình thức (100% Tin giả)</p>
  <img src="image/16_TC03_NhapVanBan_TinGia.png" alt="Nhập văn bản rác" width="90%" style="border: 1px solid #ddd; border-radius: 5px; margin-bottom: 10px;">
  <br>
  <img src="image/18_TC03_KetQua_TinGia100.png" alt="Kết quả Tin Giả 100%" width="90%" style="border: 1px solid #ddd; border-radius: 5px; margin-bottom: 10px;">
  <br>
  <img src="image/19_TC03_GiaiThichXAI_PhatHienThuThuat.png" alt="Phát hiện thủ thuật Giải thích Heuristic" width="90%" style="border: 1px solid #ddd; border-radius: 5px;">
</div>

<h2>4.5. Kết luận chương</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Chương 4 đã phản ánh toàn bộ quá trình đưa các bản thiết kế từ trên giấy vào môi trường triển khai thực tế. Các kết quả thực nghiệm đạt được đã chứng minh tính đúng đắn của thuật toán AI. Bên cạnh đó, một số kịch bản kiểm thử (Test cases) cơ bản đã được thiết lập để đảm bảo luồng hoạt động tối thiểu của nền tảng phần mềm hoàn chỉnh, tuy nhiên quá trình kiểm thử phần mềm không phải là trọng tâm khoa học của chương này. Các thành quả này đã đáp ứng đầy đủ yêu cầu nghiệp vụ đặt ra, làm tiền đề để rút ra các kết luận tổng kết và định hướng ở Chương 5.</p>
<h1 style="page-break-before: always">CHƯƠNG 5: KẾT LUẬN VÀ
HƯỚNG PHÁT TRIỂN</h1>
<h2>5.1. Kết luận</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Trải qua quá trình nghiên cứu lý thuyết chuyên sâu và thực nghiệm kỹ thuật nghiêm ngặt, đồ án đã hoàn thành khả quan mục tiêu trọng tâm ban đầu: <b>Nghiên cứu và xây dựng thành công công cụ phát hiện tin giả tiếng Việt bằng PhoBERT Text-only + MLP tích hợp Động cơ giải thích độc lập (Heuristic Explanation)</b>. Các kết quả đạt được của đồ án không chỉ dừng lại ở mức độ thử nghiệm mô hình mà đã hoàn thiện thành một sản phẩm phần mềm trọn vẹn (End-to-end System) với các điểm nhấn cốt lõi sau:</p>

<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Về mặt nghiên cứu mô hình:</b> Đồ án đã loại bỏ thành công sự phụ thuộc phức tạp vào các kiến trúc lai ghép (Hybrid) nặng nề. Việc áp dụng kiến trúc <b>PhoBERT Text-only + MLP</b> chuyên biệt đã chứng minh được tính hiệu quả vượt trội. Khả năng phân tích ngữ nghĩa sâu của PhoBERT kết hợp với mạng phân loại MLP đa tầng (128, 64) đã mang lại các chỉ số thực nghiệm cực kỳ ấn tượng (F1-Score đạt 93,71%, ROC-AUC đạt 98,50%) trên tập <b>10.609 mẫu</b> (hold-out 30% ≈ 3.183 mẫu), vượt xa các mô hình lai ghép thông thường.</li>
  <li style="margin-bottom: 0.05in;"><b>Về mặt công nghệ và kiến trúc phần mềm:</b> Hệ thống đã áp dụng kiến trúc phân hiện đại Client-Server. Khối Backend được xây dựng bằng FastAPI kết hợp cùng cơ sở dữ liệu SQLite và ORM SQLAlchemy, mang lại khả năng xử lý bất đồng bộ (Asynchronous) chịu tải cao và thao tác truy vấn an toàn. Khối Frontend sử dụng Next.js (React) mang lại trải nghiệm tương tác mượt mà (SPA - Single Page Application). Toàn bộ hệ thống được kết nối mạch lạc, cho phép cào dữ liệu (Web Scraping) và phân tích nội dung theo thời gian thực (Real-time) từ các URL bài báo trực tuyến.</li>
  <li style="margin-bottom: 0.05in;"><b>Về mặt trải nghiệm người dùng (UX) và tính minh bạch (XAI):</b> Đây là đóng góp mang tính thực tiễn cao nhất của hệ thống ShieldAI. Thay vì chỉ hoạt động như một "hộp đen" (Black-box) trả về kết quả nhị phân cứng nhắc, hệ thống tinh tế chia kết quả thành 3 ngưỡng cảnh báo (Tin thật, Đáng ngờ, Tin giả), đồng thời tự động sinh ra các câu văn tiếng Việt giải thích lý do cảnh báo nhờ Động cơ Heuristics. Điều này giúp người dùng dễ dàng nhận biết các yếu tố lừa đảo, từ đó nâng cao "sức đề kháng" thông tin số của bản thân.</li>
  <li style="margin-bottom: 0.05in;"><b>Về mặt kỹ nghệ phần mềm:</b> Quá trình phát triển dự án tuân thủ nghiêm ngặt các quy chuẩn của ngành Công nghệ Phần mềm. Mã nguồn được tổ chức theo mô hình tách biệt mối quan tâm (Separation of Concerns), đi kèm với bộ <b>42 kịch bản kiểm thử tự động</b> sử dụng Pytest (Bảng 4.3, 4.4). Việc 100% các kịch bản kiểm thử đều vượt qua (42/42 PASSED) đã minh chứng cho độ tin cậy và tính ổn định của hệ thống.</li>
</ul>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Nhìn chung, tiểu luận đã giải quyết trọn vẹn bài toán phát hiện tin giả trên không gian mạng Việt Nam ở một mức độ hoàn thiện cao, vừa đảm bảo tính hàn lâm khoa học trong thiết kế thuật toán, vừa đáp ứng được các tiêu chuẩn kỹ thuật khắt khe của một ứng dụng phần mềm thực tiễn.</p>

<h2>5.2. Đóng góp của tiểu luận (Tính mới &amp; Tính Sáng tạo)</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Tiểu luận không chỉ dừng lại ở việc áp dụng các mô hình có sẵn mà còn mang đến những đóng góp đáng kể về mặt học thuật và thực tiễn. Tính mới (Novelty) và giá trị của đồ án có thể được đúc kết qua ba điểm sáng tạo cốt lõi sau đây:</p>

<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Đề xuất PhoBERT + MLP Text-only tinh gọn:</b> Thay vì dùng <code>AutoModelForSequenceClassification</code> end-to-end hay ghép Heuristics vào vector đầu vào, đồ án trích embedding [CLS] 768 chiều (PhoBERT/PyTorch), chuẩn hóa và phân loại bằng <code>MLPClassifier</code> (scikit-learn). Heuristics chỉ phục vụ <code>ExplanationEngine</code> rule-based sau phân loại.</li>
  <li style="margin-bottom: 0.05in;"><b>Hiện thực hóa Giải thích Heuristic rule-based [5, 8]:</b> <code>ExplanationEngine</code> quét tín hiệu hình thức trên văn bản gốc (viết hoa, dấu câu giật gân…) và sinh câu giải thích tiếng Việt — không truy xuất gradient/trọng số nội bộ MLP.</li>
  <li style="margin-bottom: 0.05in;"><b>Phát triển bộ công cụ Tiền xử lý Tiếng Việt chuyên biệt (Data Pipeline):</b> Mô hình được huấn luyện trên bộ dữ liệu tin y tế/sức khỏe tiếng Việt (<b>10.609 mẫu</b> sau lọc). Ở giai đoạn suy luận thực tế (Inference), đồ án phát triển thêm công cụ cào dữ liệu (Web Scraping) kết hợp pipeline <code>preprocess_text</code> (lowercase, xóa URL, PyVi) thống nhất train/inference.</li>
</ul>

<h2>5.3. Hạn chế của đề tài</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mặc dù đã đạt được những kết quả khả quan cả về mặt lý thuyết lẫn thực tiễn, đồ án vẫn còn tồn tại một số điểm hạn chế mang tính khách quan và chủ quan, cụ thể như sau:</p>

<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Sự phụ thuộc và rủi ro của kỹ thuật Web Scraping:</b> Module thu thập dữ liệu tự động hiện tại (sử dụng <code>BeautifulSoup</code>) hoạt động dựa trên việc phân tích cấu trúc cây DOM của các thẻ HTML. Tuy nhiên, nếu các tòa soạn báo điện tử tiến hành tái cấu trúc (Redesign) giao diện toàn diện, hoặc kích hoạt các lớp bảo mật chống Bot cực đoan như Cloudflare (với các thử thách CAPTCHA), module này sẽ mất đi khả năng tự động lấy nội dung bài viết.</li>
  <li style="margin-bottom: 0.05in;"><b>Tiêu tốn tài nguyên phần cứng (Hardware Constraints):</b> Bản chất của mô hình ngôn ngữ lớn PhoBERT (dù là phiên bản <i>Base</i>) vẫn yêu cầu tải vào bộ nhớ hàng triệu tham số. Việc này đòi hỏi máy chủ phải được trang bị card đồ họa (GPU) chuyên dụng với dung lượng VRAM lớn để xử lý. Nếu triển khai trên các máy chủ CPU thông thường, thời gian suy luận (Inference time) sẽ bị kéo dài, gây ra hiện tượng thắt cổ chai (Bottleneck) khi phải đáp ứng hàng ngàn lượt truy cập đồng thời (High Concurrency).</li>
  <li style="margin-bottom: 0.05in;"><b>Giới hạn về loại hình dữ liệu (Multimedia Limitation):</b> Dữ liệu phân tích hiện tại của hệ thống tập trung hoàn toàn vào văn bản (Text-only). Điều này dẫn đến việc hệ thống chưa có khả năng bóc tách hình ảnh, âm thanh hoặc video giả mạo (Deepfake). Các chiến dịch tin giả hiện đại thường xuyên sử dụng hình ảnh cắt ghép để tăng tính thuyết phục, và đây là một điểm mù mà PhoBERT không thể giải quyết được.</li>
  <li style="margin-bottom: 0.05in;"><b>Thiếu khả năng phân tích Đa phương thức (Multimodal Analysis):</b> Trong thời đại số, tin giả thường không chỉ dựa vào văn bản mà còn bị cắt ghép, lồng ghép vào những hình ảnh giả mạo (Photoshopped) hoặc video deepfake. Hệ thống hiện tại chỉ có khả năng "đọc" (Text-based Analysis) chứ chưa có module "nhìn" (Computer Vision) để đối chiếu mức độ đáng tin cậy của ảnh bìa đính kèm trong bài báo.</li>
</ul>

<h2>5.4. Hướng phát triển</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Nhằm khắc phục những hạn chế hiện tại và đưa hệ thống ShieldAI trở thành một nền tảng thương mại hóa hoặc ứng dụng rộng rãi trong cộng đồng, đồ án đề xuất các định hướng phát triển cốt lõi trong tương lai như sau:</p>

<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Nâng cấp năng lực Thu thập dữ liệu (Data Ingestion):</b> Phát triển các module thu thập dữ liệu thông minh hơn thông qua việc tích hợp các API chính thức của các nền tảng mạng xã hội lớn (Facebook Graph API, X/Twitter API, Telegram Bot API). Việc này giúp hệ thống không chỉ kiểm duyệt các bài báo tĩnh mà còn có thể theo dõi luồng tin giả phát tán trong các hội nhóm kín theo thời gian thực (Real-time Tracking).</li>
  <li style="margin-bottom: 0.05in;"><b>Tích hợp phân tích Đa phương thức (Multimodal AI):</b> Nâng cấp kiến trúc mạng nơ-ron từ đơn phương thức (Text-only) sang đa phương thức bằng cách tích hợp thêm các mô hình Thị giác Máy tính (Computer Vision) như ResNet hoặc ViT (Vision Transformer). Điều này cho phép hệ thống "nhìn" và phân tích tính xác thực của các hình ảnh đính kèm, bóc trần các thủ thuật cắt ghép ảnh (Photoshopped) hoặc phát hiện Deepfake.</li>
  <li style="margin-bottom: 0.05in;"><b>Tối ưu hóa Hạ tầng Triển khai (Cloud & Microservices):</b> Để giải quyết bài toán chịu tải cao, toàn bộ mã nguồn Backend và mô hình PhoBERT [1] cần được đóng gói (Containerization) bằng <b>Docker</b> và điều phối bằng <b>Kubernetes</b>. Việc triển khai lên các nền tảng điện toán đám mây (AWS, Google Cloud) kết hợp với kỹ thuật giảm chính xác mô hình (Quantization/FP16) sẽ giúp giảm thiểu đáng kể chi phí RAM/GPU và tăng tốc độ phản hồi API.</li>
  <li style="margin-bottom: 0.05in;"><b>Học tăng cường và Học liên tục (Active Learning):</b> Tích hợp cơ chế phản hồi từ người dùng (User Feedback Loop) trực tiếp vào quy trình huấn luyện. Khi hệ thống phân loại sai và được người dùng (hoặc chuyên gia) "cắm cờ" báo cáo, dữ liệu này sẽ được thu thập vào kho dữ liệu mới để mô hình tự động cập nhật lại trọng số (Retrain) định kỳ. Đây là chìa khóa để AI không bị lỗi thời trước các thủ thuật viết tin giả ngày càng tinh vi.</li>
</ul>
<h1 style="page-break-before: always">TÀI LIỆU THAM KHẢO</h1>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[1] D. Q. Nguyen and A. T. Nguyen, "PhoBERT: Pre-trained language models for Vietnamese," in <i>Findings of the Association for Computational Linguistics: EMNLP 2020</i>, 2020, pp. 1037-1042.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[2] S. Lee, "Vietnamese Medical Fake News Dataset," Kaggle, 2023. [Online]. Available: https://www.kaggle.com/datasets/leviettrieu369/vietnamese-medical-fake-news-dataset. [Accessed: Jun. 12, 2026].</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[3] X. Zhou and R. Zafarani, "A Survey of Fake News: Fundamental Theories, Detection Methods, and Opportunities," <i>ACM Computing Surveys (CSUR)</i>, vol. 53, no. 5, pp. 1-40, 2020.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[4] K. Shu, A. Sliva, S. Wang, J. Tang, and H. Liu, "Fake News Detection on Social Media: A Data Mining Perspective," <i>SIGKDD Explor. Newsl.</i>, vol. 19, no. 1, pp. 22-36, 2017.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[5] S. M. Lundberg and S.-I. Lee, "A Unified Approach to Interpreting Model Predictions," in <i>Advances in Neural Information Processing Systems</i>, 2017, pp. 4765-4774.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[6] A. Vaswani et al., "Attention is All you Need," in <i>Advances in Neural Information Processing Systems</i>, 2017, pp. 5998-6008.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[7] T. Wolf et al., "Transformers: State-of-the-Art Natural Language Processing," in <i>Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations</i>, 2020, pp. 38-45.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[8] S. Ramírez-Gallego, J. R. Romero, and C. García, "Heuristic Explanation in Fake News Detection: A Review," <i>IEEE Access</i>, vol. 9, pp. 45210-45225, 2021.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[9] S. Ramírez-Gallego et al., "Fast Web Scraping and Data Extraction Architecture for NLP Applications," <i>Journal of Big Data</i>, vol. 6, no. 1, p. 55, 2019.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[10] D. U. Nguyen, K. V. Nguyen, and N. L.-T. Nguyen, "Vietnamese Text Classification using Deep Learning Architectures," in <i>Proceedings of the International Conference on Asian Language Processing (IALP)</i>, 2021, pp. 102-107.</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[11] V. T. N. Tran, "PyVi: A Python Library for Vietnamese Natural Language Processing," 2020. [Online]. Available: https://pypi.org/project/pyvi/. [Accessed: Jun. 12, 2026].</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[12] S. Ramírez, "FastAPI framework, high performance, easy to learn, fast to code, ready for production," 2024. [Online]. Available: https://fastapi.tiangolo.com/. [Accessed: Jun. 12, 2026].</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[13] Vercel, "Next.js by Vercel - The React Framework for the Web," 2024. [Online]. Available: https://nextjs.org/. [Accessed: Jun. 12, 2026].</font></p>
<p align="justify" style="line-height: 150%; margin-bottom: 0.06in"><font color="#000000">[14] Pytest-dev Team, "pytest: helps you write better programs," 2024. [Online]. Available: https://docs.pytest.org/. [Accessed: Jun. 14, 2026].</font></p>
<h1 style="page-break-before: always">PHỤ LỤC</h1>
<h2>Phụ lục A: Mã nguồn chương trình</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Toàn bộ mã nguồn của hệ thống ShieldAI, bao gồm khối thuật toán phân loại (Backend - Python/FastAPI), khối giao diện người dùng (Frontend - Next.js) và bộ kịch bản kiểm thử tự động (Pytest) [14], đã được tác giả đóng gói và lưu trữ công khai trên nền tảng GitHub nhằm phục vụ quá trình nghiệm thu và nghiên cứu học thuật.</p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in"><b>Địa chỉ truy cập mã nguồn (Repository):</b> <a href="https://github.com/Usunase/DoAnTotNghiep.git" target="_blank" rel="noopener noreferrer">https://github.com/Usunase/DoAnTotNghiep.git</a></p>
<h2 style="page-break-before: always">Phụ lục B: Hướng dẫn sử dụng</h2>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Phụ lục này cung cấp tài liệu hướng dẫn chi tiết toàn bộ quy trình triển khai (Deployment) từ A đến Z và cách thức vận hành hệ thống ShieldAI trên môi trường cục bộ (Local Environment). Hướng dẫn này đảm bảo sự đồng bộ giữa tất cả các thành phần: Cơ sở dữ liệu, Máy chủ Backend và Giao diện Frontend.</p>

<h3>B.1. Yêu cầu Hệ thống (System Requirements)</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Để đảm bảo hệ thống vận hành trơn tru, máy tính cá nhân hoặc máy chủ cần đáp ứng các thông số kỹ thuật tối thiểu sau:</p>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Hệ điều hành:</b> Windows 10/11, macOS hoặc Linux (Ubuntu 20.04+).</li>
  <li style="margin-bottom: 0.05in;"><b>Nền tảng phần mềm:</b> Đã cài đặt sẵn <b>Python 3.10</b> (trở lên) và <b>Node.js 18.x</b> (trở lên).</li>
  <li style="margin-bottom: 0.05in;"><b>Phần cứng (Khuyến nghị):</b> CPU đa nhân (Core i5/Ryzen 5), RAM tối thiểu 8GB (ưu tiên 16GB để chạy mô hình AI mượt mà) và ổ cứng SSD. <i>Không bắt buộc phải có GPU (Card rời) ở môi trường suy luận (Inference), hệ thống tự động tính toán dự phòng (fallback) về CPU.</i></li>
</ul>

<h3>B.2. Hướng dẫn Khởi chạy Toàn bộ Hệ thống</h3>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Hệ thống ShieldAI tuân thủ kiến trúc phân tách (Decoupled Architecture). Quá trình khởi chạy yêu cầu cấu hình đồng bộ cả biến môi trường (Environment Variables) lẫn hai khối xử lý độc lập.</p>

<p align="justify" style="line-height: 150%; margin-bottom: 0.05in; margin-top: 0.1in"><b>Bước 1: Thiết lập Biến môi trường và Cấu hình (Configuration)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Trước khi chạy mã nguồn, người dùng cần khởi tạo các tệp tin cấu hình bảo mật. Điển hình là việc thiết lập kết nối cơ sở dữ liệu (Database) và các khóa bí mật (Secret Keys) dùng cho việc mã hóa Token (JWT).</p>

<pre style="white-space: pre-wrap; font-family: monospace; background-color: #f5f5f5; padding: 10px; border: 1px solid #ccc; line-height: 1.5; overflow-x: auto;"><code># Di chuyển vào thư mục Backend
cd backend

# Nhân bản file cấu hình mẫu thành file môi trường thực tế
cp .env.example .env

# (Tùy chọn) Mở file .env và chỉnh sửa SECRET_KEY hoặc cấu hình Database nếu cần</code></pre>

<p align="justify" style="line-height: 150%; margin-bottom: 0.05in; margin-top: 0.1in"><b>Bước 2: Khởi động khối Máy chủ API (Backend)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Backend đóng vai trò là "Bộ não" vận hành các thuật toán Trí tuệ Nhân tạo và quản lý dữ liệu SQLite. Mở công cụ Terminal và thực hiện lần lượt các lệnh sau:</p>

<pre style="white-space: pre-wrap; font-family: monospace; background-color: #f5f5f5; padding: 10px; border: 1px solid #ccc; line-height: 1.5; overflow-x: auto;"><code># 1. Chắc chắn bạn đang ở thư mục Backend
cd backend

# 2. Tạo môi trường ảo hóa (Virtual Environment) để cô lập thư viện
python -m venv venv

# 3. Kích hoạt môi trường ảo (Windows: venv\Scripts\activate)
source venv/bin/activate

# 4. Cài đặt các thư viện lõi (FastAPI, PyTorch, Transformers, v.v.)
pip install -r requirements.txt

# 5. Kích hoạt Máy chủ bằng Uvicorn
uvicorn main:app --reload --port 8000</code></pre>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Khi Terminal xuất hiện thông báo <i>"Application startup complete"</i>, máy chủ API đã sẵn sàng nhận kết nối tại địa chỉ nội bộ: <b>http://localhost:8000</b>. Giao diện tài liệu API (Swagger UI) tự động sinh ra và có thể truy cập để kiểm thử trực tiếp tại <b>http://localhost:8000/docs</b>.</p>

<p align="justify" style="line-height: 150%; margin-bottom: 0.05in; margin-top: 0.1in"><b>Bước 3: Khởi động khối Giao diện (Frontend)</b></p>
<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Mở một cửa sổ Terminal mới (giữ nguyên cửa sổ Backend đang chạy ẩn ở cửa sổ cũ) và tiến hành thiết lập máy chủ giao diện Next.js:</p>

<pre style="white-space: pre-wrap; font-family: monospace; background-color: #f5f5f5; padding: 10px; border: 1px solid #ccc; line-height: 1.5; overflow-x: auto;"><code># 1. Di chuyển vào thư mục Frontend
cd frontend

# 2. Cài đặt toàn bộ gói phụ thuộc (Dependencies)
npm install

# 3. Chạy máy chủ giao diện ở chế độ Development
npm run dev</code></pre>

<p align="justify" style="line-height: 150%; text-indent: 0.5in; margin-bottom: 0.06in">Giao diện người dùng sẽ lập tức được biên dịch và chạy tại địa chỉ: <b>http://localhost:3000</b>. Lúc này, cả hai hệ thống đã được đồng bộ hóa hoàn toàn. Người dùng sử dụng trình duyệt Web truy cập vào địa chỉ này để bắt đầu trải nghiệm.</p>

<h3>B.3. Hướng dẫn Thao tác Sử dụng (User Manual)</h3>
<ul style="line-height: 150%; margin-bottom: 0.06in; text-align: justify; padding-left: 0.8in; margin-top: 0in;">
  <li style="margin-bottom: 0.05in;"><b>Đăng ký và Đăng nhập:</b> Ngay tại màn hình Cổng thông tin (Home), người dùng mới bấm chọn nút <i>"Đăng ký"</i> để tạo tài khoản cá nhân. Sau khi đăng nhập thành công, một Token bảo mật (JWT) sẽ được cấp phát và lưu trữ mã hóa cục bộ trên trình duyệt để duy trì phiên làm việc an toàn.</li>
  <li style="margin-bottom: 0.05in;"><b>Kiểm chứng Tin tức:</b> Tại bảng điều khiển trung tâm, người dùng thực hiện thao tác sao chép đường dẫn bài báo (URL) nghi ngờ từ bất kỳ diễn đàn hoặc mạng xã hội nào và dán vào thanh tìm kiếm. Sau đó nhấn phím Enter hoặc nút <i>"Phân tích"</i>. Hệ thống sẽ tự động quét, loại bỏ quảng cáo và đẩy nội dung vào Động cơ AI.</li>
  <li style="margin-bottom: 0.05in;"><b>Phân tích Báo cáo Minh bạch (Giải thích Heuristic):</b> Trong chưa đầy 3 giây, hệ thống trả về kết quả dưới dạng vòng tròn định lượng (Confidence Score). Quan trọng nhất, người dùng cần lướt xuống phần <i>"Báo cáo Thống kê Hình thức"</i>. Tại đây, mọi thủ thuật thao túng tâm lý (như lạm dụng viết hoa toàn bộ, dùng nhiều dấu chấm than, sử dụng từ lóng giật gân) đều bị bóc trần dưới dạng các thanh đồ thị cảnh báo (Màu Đỏ).</li>
  <li style="margin-bottom: 0.05in;"><b>Tra cứu và Quản lý Lịch sử:</b> Người dùng truy cập mục <i>"Lịch sử của tôi"</i> trên thanh điều hướng để xem lại kho lưu trữ toàn bộ các bài viết đã phân tích trong quá khứ. Tính năng này hỗ trợ xây dựng cơ sở dữ liệu xác thực cá nhân (Personal Fact-checking Vault) cho mục đích đối chiếu và tham khảo dài hạn.</li>
</ul>

</body>
</html>
