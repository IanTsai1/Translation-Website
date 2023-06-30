const record = document.querySelector(".record");
const stop = document.querySelector(".stop");
const soundClips = document.querySelector(".sound-clips");

if (navigator.mediaDevices.getUserMedia) {
  console.log('getUserMedia supported.');

  const constraints = { audio: true };
  let chunks = [];

  let onSuccess = function(stream) {
    const mediaRecorder = new MediaRecorder(stream);

    visualize(stream);

    record.onclick = function() {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("recorder started");
      record.style.background = "red";

      stop.disabled = false;
      record.disabled = true;
    }

    stop.onclick = function() {
      mediaRecorder.stop();
      console.log(mediaRecorder.state);
      console.log("recorder stopped");
      record.style.background = "";
      record.style.color = "";
      // mediaRecorder.requestData();

      stop.disabled = true;
      record.disabled = false;
    }
    mediaRecorder.onstop = function(e) {
      console.log("data available after MediaRecorder.stop() called.");
      const blob = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
      chunks = [];
      const audioURL = window.URL.createObjectURL(blob);

      const downloadLink = document.createElement("a");
      downloadLink.href = audioURL;
      downloadLink.download = "tmp.ogg";

      downloadLink.style.display = "none"; // Hide the download link

      document.body.appendChild(downloadLink); // Append the link to the document body
      downloadLink.click(); // Trigger the click event

      document.body.removeChild(downloadLink); // Clean up by removing the link from the document body
    };
  }
}






