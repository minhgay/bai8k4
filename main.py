st.title("tàu hàng liều lĩnh đi qua eo biển ")

tin1 ='Các công ty có thể kiếm hàng triệu USD cho mỗi chuyến tàu qua eo biển Hormuz, bất chấp phí bảo hiểm và lương thủy thủ cao.'
st.write(tin1)
tin2 = 'Ngày 13/3, Reuters trích dữ liệu của các công ty theo dấu tàu biển Lloyd’s List Intelligence và MarineTraffic cho thấy ít nhất 10 tàu do các công ty Hy Lạp vận hành và ít nhất 2 tàu do Trung Quốc vận hành đã đi qua eo biển Hormuz từ khi xung đột tại Trung Đông xảy ra ngày 28/2. Số tàu này chở cả dầu và hàng hóa thông thường.'
st.write(tin2)
and = 'https://i1-kinhdoanh.vnecdn.net/2026/03/14/iran-tanker-1773463485-7413-1773463537.jpg?w=680&h=0&q=100&dpr=2&fit=crop&s=2DGMCCcPUSFz8RoNH6Jl8g'
st.image(anh,'caption(Các tàu dầu ở vùng biển gần eo biển Hormuz ngày 11/3. Ảnh: Reuter))
#sound
if st.button('đọc nội dung'):
    tts= gTTS(text=tin1+tin2,lang='vi')
    output_file='output_file'
    audio_file = open(output_file,'rb'#open binary binary file 
    mp3 = audio.file.read()# đọc toàn bộ 
    st.audio(mp3,format='audio/mp3')
    
st.write('video minh hoa ')
st.video('https://www.youtube.com/watch?v=5PHGGUMzAu0',format='video/mp4')
