let autocomplete;

function initAutoComplete(){
autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('id_address'),
    {
        types: ['geocode', 'establishment'],
        //default in this app is "IN" - add your country code
        componentRestrictions: {'country': ['in']},
    })
// function to specify what should happen when the prediction is clicked
autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged (){
    var place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert()
    if (!place.geometry){
        document.getElementById('id_address').placeholder = "Start typing...";
    }
    else{
        console.log('place name=>', place.name)
    }
    // get the address components and assign them to the fields
}


// $(document).ready(function(){
//     $('.add_to_cart').on('click', function(e){
//         e.preventDefault();
        
//         food_id = $(this).attr('data-id')
//         url = $(this).attr('data-url');
//         data = {
//             food_id:food_id,
//         }

//         $.ajax({
//             type: 'GET',
//             url: url,
//             data: data,
//             success: function(response){
//                 console.log(response)
//             }
//         })
//     })
// });

// Define the data we want to send
const data = {
                type: 'POST',
                url: url,
                data: data,
                success: function(response){
                    console.log(response)
                }};
  
  // Send the POST request using fetch
  fetch("add_to_cart/food_id", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .then((response) => response.json())
    .then((data) => console.log("Success:", data))
    .catch((error) => console.error("Error:", error));



    var generateBtn = document.getElementById('generateSP');
    generateBtn.addEventListener('click', fetchData);
    
    function fetchData() {
       fetch('add_to_cart/food_id/')
        .then(function (response) {
          if (response.status !== 200) {
            console.log(
              'Looks like there was a problem. Status Code: ' + response.status
            );
            return;
          }
          response.json().then(function (data) {
            console.log(data);
            document.getElementById('w3review').value = data;
          });
        })
        .catch(function (err) {
          console.log('Fetch Error :-S', err);
        });
    }

