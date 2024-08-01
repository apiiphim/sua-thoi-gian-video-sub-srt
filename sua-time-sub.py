import re

def adjust_srt_timing(file_path, offset_seconds):
    time_pattern = re.compile(r"(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})")
    
    def time_to_ms(hours, minutes, seconds, milliseconds):
        return (int(hours) * 3600 + int(minutes) * 60 + int(seconds)) * 1000 + int(milliseconds)
    
    def ms_to_time(milliseconds):
        hours = milliseconds // 3600000
        milliseconds %= 3600000
        minutes = milliseconds // 60000
        milliseconds %= 60000
        seconds = milliseconds // 1000
        milliseconds %= 1000
        return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    adjusted_lines = []
    for line in lines:
        match = time_pattern.match(line)
        if match:
            start_time = time_to_ms(*match.groups()[:4])
            end_time = time_to_ms(*match.groups()[4:])
            
            start_time = max(0, start_time - offset_seconds * 1000)
            end_time = max(0, end_time - offset_seconds * 1000)
            
            new_start_time = ms_to_time(start_time)
            new_end_time = ms_to_time(end_time)
            
            adjusted_lines.append(f"{new_start_time} --> {new_end_time}\n")
        else:
            adjusted_lines.append(line)
    
    output_path = f"apiionline_{file_path.split('\\')[-1]}"
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(adjusted_lines)
    
    print(f"Adjusted SRT file saved as {output_path}")

# Bắt đầu từ giây bao nhiêu để điều chỉnh
adjust_srt_timing(r'C:\Users\trong\Downloads\a\a.srt', 41)
