
const BASE_URL = "http://127.0.0.1:5000/api";

function generateCupcakeHTML(cupcake) {
   return `
      <div data-cupcake-id=${cupcake.id}>
         <li>
            ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating} - <button class="delete-cupcake">X</button>
         </li>
         <img class="Cupcake-img"
            src="${cupcake.image}"
            alt="(no image provided)">
      </div>
   `

}

async function showCupcakes() {
   const resp = await axios.get(`${BASE_URL}/cupcakes`)

   for (let cupcakeData of resp.data.cupcakes) {
      let newCupcake = $(generateCupcakeHTML(cupcakeData))
      $('#cupcake-list').append(newCupcake)
   }
}

// handle form submit
$("#new-cupcake-form").on("submit", async function (evt) {
   evt.preventDefault();

   let flavor = $("#form-flavor").val();
   let rating = $("#form-rating").val();
   let size = $("#form-size").val();
   let image = $("#form-image").val();

   const resp = await axios.post(`${BASE_URL}/cupcakes`, {
      flavor,
      rating,
      size,
      image
   });

   let newCupcake = $(generateCupcakeHTML(resp.data.cupcake));
   $("#cupcake-list").append(newCupcake);
   $("#new-cupcake-form").trigger("reset");
});

$('#cupcake-list').on("click", ".delete-cupcake", async function (e) {
   e.preventDefault()

   let cupcake = $(e.target).closest("div")
   let cupcakeID = cupcake.attr("data-cupcake-id")
   await axios.delete(`${BASE_URL}/cupcakes/${cupcakeID}`)
   cupcake.remove()
})

$(showCupcakes);