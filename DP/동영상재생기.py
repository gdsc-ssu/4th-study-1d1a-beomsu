def next(cur_minutes, cur_seconds, video_end_minutes, video_end_seconds):
    next_seconds = cur_seconds + 10
    next_minutes = cur_minutes
    
    if next_seconds >= 60:
        next_minutes += 1
        next_seconds -= 60
    
    if (next_minutes, next_seconds) > (video_end_minutes, video_end_seconds):
        return video_end_minutes, video_end_seconds
    
    return next_minutes, next_seconds

def prev(cur_minutes, cur_seconds):
    prev_seconds = cur_seconds - 10
    prev_minutes = cur_minutes
    
    if prev_seconds < 0:
        prev_minutes -= 1
        prev_seconds += 60
    
    if prev_minutes < 0:
        return 0, 0
    
    return prev_minutes, prev_seconds

def is_in_opening(cur_minutes, cur_seconds, op_start_minutes, op_start_seconds, op_end_minutes, op_end_seconds):
    return ((op_start_minutes, op_start_seconds) <= (cur_minutes, cur_seconds) <= (op_end_minutes, op_end_seconds))

def solution(video_len, pos, op_start, op_end, commands):
    video_end_minutes, video_end_seconds = map(int, video_len.split(":"))
    cur_minutes, cur_seconds = map(int, pos.split(":"))
    op_start_minutes, op_start_seconds = map(int, op_start.split(":"))
    op_end_minutes, op_end_seconds = map(int, op_end.split(":"))
    
    if is_in_opening(cur_minutes, cur_seconds, op_start_minutes, op_start_seconds, op_end_minutes, op_end_seconds):
        cur_minutes, cur_seconds = op_end_minutes, op_end_seconds

    for command in commands:
        if command == "next":
            cur_minutes, cur_seconds = next(cur_minutes, cur_seconds, video_end_minutes, video_end_seconds)
        elif command == "prev":
            cur_minutes, cur_seconds = prev(cur_minutes, cur_seconds)
        
        if is_in_opening(cur_minutes, cur_seconds, op_start_minutes, op_start_seconds, op_end_minutes, op_end_seconds):
            cur_minutes, cur_seconds = op_end_minutes, op_end_seconds
    
    answer_minutes = f"{cur_minutes:02}"
    answer_seconds = f"{cur_seconds:02}"
    return f"{answer_minutes}:{answer_seconds}"
