# audio-recognition-quick-trial
<a href="www.acrcloud.com">ACRCloud</a> is a cloud platform that helps excellent companies and developers integrate the most advanced ACR (Automatic Content Recognition) techniques into their products to get the abilities to recognize audios and videos, monitor radio streams, detect live TV contents and so on.
<pre>
<a href="https://github.com/acrcloud">Cross-platform SDKs</a> and <a href="http://docs.acrcloud.com/">Documents</a>. 
Contact us (<a href="mailto:contact@acrcloud.com">contact@acrcloud.com</a>) if you have any questions.
</pre>

This repository contains step-by-step instructions of common audio recognition use cases. 

<a href="https://github.com/acrcloud-demo/audio-recognition-quick-trial/archive/master.zip">Download</a> or clone this repository to start (Linux x86-64 Environment needed).

<h3>Recognise Recorded Audio Snippet ( with noise )</h3>
<strong>Step 1</strong>

<a target="_blank" href="http://console.acrcloud.com/signup">Register</a> an free account and login.

Create an "Audio & Video Recognition" project and select options as the follow picture (Make sure the "ACRCloud Music" bucket is selected). <br>
Save the <strong>access_key</strong> and <strong>access_key</strong> of the project for further use.
![image](https://github.com/acrcloud-demo/audio-recognition-quick-trial/blob/master/create_project.png)

<strong>Step 2</strong>

Edit <strong>test.py</strong> and replace '<...>' in the two lines below with <strong>access_key</strong> and <strong>access_key</strong> you saved.

<code>'access_key':'\<access_key of your project\>',</code><br>
<code>'access_secret':'\<access_secret of your project\>',</code>

Save the changes.

<strong>Step 3</strong>

Run the script: 
<code>python test.py audio_with_noise.wav</code>

Result will be: 
<pre>
recognizing by file ...
{"status":{"msg":"Success","code":0,"version":"1.0"},"metadata":{"music":[{"external_ids":{"isrc":"USAT21500254","upc":"075679928634"},"play_offset_ms":46360,"external_metadata":{"spotify":{"album":{"id":"0HfAFdxzAEOn1H9WQeaqgZ"},"artists":[{"id":"6VuMaDnrHyPL1p4EHjYLi7"},{"id":"6JL8zeS1NmiOftqZTRgdTz"}],"track":{"id":"1zxFtsKWwuVpz3nSqNYshe"}},"deezer":{"album":{"id":9602354},"artists":[{"id":1362735}],"genres":[{"id":132}],"track":{"id":94424876}}},"label":"Artist Partners","release_date":"2015-02-10","title":"Marvin Gaye (feat. Meghan Trainor)","duration_ms":"187741","album":{"name":"Marvin Gaye (feat. Meghan Trainor)"},"acrid":"aa1c08067d9e3071f8a4d319fc186cb3","genres":[{"name":"Pop"}],"artists":[{"name":"Charlie Puth"}]}],"timestamp_utc":"2015-12-01 09:41:32"},"result_type":0}
</pre>
audio_with_noise.wav is recognised to be: "Marvin Gaye (feat. Meghan Trainor)" of "Charlie Puth".

<h3>Recognise Original Audio Snippet ( without noise )</h3>

<strong>Step 1</strong>

Create another project and select "Line-in Audio (Audio of original file or stream without noise)" for "Client-End Audio Source" option.
![image](https://github.com/acrcloud-demo/audio-recognition-quick-trial/blob/master/create_project_2.png)

<strong>Step 2</strong>

Edit <strong>test.py</strong> with <strong>access_key</strong> and <strong>access_key</strong> of this project and save it.

<strong>Step 3</strong>

Run the script: 
<code>python test.py audio_without_noise.wav</code>

Result will be:
<pre>
recognizing by file ...
{"status":{"msg":"Success","code":0,"version":"1.0"},"metadata":{"music":[{"external_ids":{"isrc":"USSM11500753","upc":"886445105360"},"play_offset_ms":46880,"external_metadata":{"spotify":{"album":{"id":"39WI8tjY7vH68xrNiDKNly"},"artists":[{"id":"3QLIkT4rD2FMusaqmkepbq"}],"track":{"id":"1m0E5D8cOJyO1A2IBX4w4i"}},"itunes":{"album":{"id":991946506},"artists":[{"id":431528675}],"track":{"id":991946508}},"deezer":{"album":{"id":9679444},"artists":[{"id":427604}],"genres":[{"id":132}],"track":{"id":95138146}}},"label":"Columbia","release_date":"2015-02-13","title":"Fight Song","duration_ms":"204066","album":{"name":"Fight Song"},"acrid":"7c8d984cfa4fd9f070da057875f09897","genres":[{"name":"Pop"}],"artists":[{"name":"Rachel Platten"}]}],"timestamp_utc":"2015-12-01 09:47:47"},"result_type":0}
</pre>
audio_without_noise.wav is recognised to be: "Fight Song" of "Rachel Platten".



