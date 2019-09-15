

var name = document.getElementById("mainText").value;
	  var id = document.getElementById("mainID").value;
	  var postData= {
	  	name: name,
	  	
	  }
	  var newPostKey = firebase.database().ref().child(id).push().key;
	  var updates ={};
	  updates[id+" "+newPostKey] = postData;
	  
	  return firebase.database().ref().update(updates)





 var name = document.getElementById("mainText").value;
	  var id = document.getElementById("mainID").value;
	  firebase.database().ref("Student: "+id).set({
	  	username: name
	  }); 
	  	


