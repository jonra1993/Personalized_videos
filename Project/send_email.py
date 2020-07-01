from mailchimp3 import MailChimp

client = MailChimp(mc_api='5c7105acb2d0019d9c5e30fb7a2da49d-us10', mc_user='JennyCGT')

['ffmpeg', '-y', '-i', '/home/jenny/Documents/GITHUB/Personalized_videos/Project/assets/base_video.mp4', 
'-i', 'Project/assets/fondo.mp3', '1:a:0', 
'-f', 'image2', '-loop', '1', '-itsoffset', '1', '-t', '4.0', '-i', 'Project/assets/rj.png', 
'-f', 'image2', '-loop', '1', '-itsoffset', '0.0', '-t', '5.0', '-i', '/tmp/vogon_t1fm9eb3.png', 
'-f', 'image2', '-loop', '1', '-itsoffset', '5.0', '-t', '10.0', '-i', '/tmp/vogon_2bwp5fwq.png', 
'-f', 'image2', '-loop', '1', '-itsoffset', '5.0', '-t', '10.0', '-i', '/tmp/vogon_li7m6ld0.png', 
'-filter_complex', 
"[1:v] format=rgba,scale=500:-1 [vid_1_resized];[vid_1_resized] fade=t=in:st=1.0q2:d=1.0:alpha=1 [vid_1_fadedin];[vid_1_fadedin] fade=t=out:st=4.0:d=1.0:alpha=1 [vid_1_fadedout];[0:v][vid_1_fadedout] overlay=700-overlay_w/2:300:enable='between(t,1.0,5.0)' [ov_0];
[2:v] format=rgba,scale=iw/4:ih/4 [vid_2_resized];[vid_2_resized] fade=t=in:st=0.0:d=1.0:alpha=1 [vid_2_fadedin];[vid_2_fadedin] fade=t=out:st=4.0:d=1.0:alpha=1 [vid_2_fadedout];[ov_0][vid_2_fadedout] overlay=1000-overlay_w/2:200:enable='between(t,0.0,5.0)' [ov_1];
[3:v] format=rgba,scale=iw/4:ih/4 [vid_3_resized];[vid_3_resized] fade=t=in:st=5.0:d=1.0:alpha=1 [vid_3_fadedin];[vid_3_fadedin] fade=t=out:st=14.0:d=1.0:alpha=1 [vid_3_fadedout];[ov_1][vid_3_fadedout] overlay=1000-overlay_w/2:150:enable='between(t,5.0,15.0)'[ov_2];
[4:v] format=rgba,scale=iw/4:ih/4 [vid_4_resized];[vid_4_resized] fade=t=in:st=5.0:d=1.0:alpha=1 [vid_4_fadedin];[vid_4_fadedin] fade=t=out:st=14.0:d=1.0:alpha=1 [vid_4_fadedout];[ov_2][vid_4_fadedout] overlay=1000-overlay_w/2:700:enable='between(t,5.0,15.0)'", 
'Project/output/video1.mp4']

ffmpeg -y -i /home/jenny/Documents/GITHUB/Personalized_videos/Project/assets/base_video.mp4 -i Project/assets/audio.mp3 -map 0:0 -c:a aac -strict -2  -c:v copy  Project/output/video1.mp4
