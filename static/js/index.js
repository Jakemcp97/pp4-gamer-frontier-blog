var myWidget = cloudinary.createUploadWidget({
    cloudName: 'dwi0ve77m', 
    uploadPreset: 'my_preset'}, (error, result) => { 
      if (!error && result && result.event === "success") { 
        console.log('Done! Here is the image info: ', result.info); 
      }
    }
  )
  
  document.getElementById("upload_widget").addEventListener("click", function(){
      myWidget.open();
    }, false);