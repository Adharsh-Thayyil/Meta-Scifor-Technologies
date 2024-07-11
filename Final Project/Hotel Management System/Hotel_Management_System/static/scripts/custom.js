$(document).ready(function(){
    
    // Add To Selection
    $(".add-to-selection").on("click", function(){

        let button = $(this)
        let id = button.attr("data-index")

        let hotel_id = $("#id").val()
        let room_id = $(`.room_id_${id}`).val()
        let room_number = $(`.room_number_${id}`).val()
        let hotel_name = $("#hotel_name").val()
        let room_name = $("#room_name").val()
        let room_price = $("#room_price").val()
        let number_of_beds = $("#number_of_beds").val()
        let room_type = $("#room_type").val()
        let checkin = $("#checkin").val()
        let checkout = $("#checkout").val()
        let adult = $("#adult").val()
        let children = $("#children").val()

        console.log(`${id} Added To Selection`);
        console.log(`hotel_id: ${hotel_id}`);
        console.log(`room_number: ${room_number}`);
        console.log(`room_id: ${room_id}`);
        console.log(`hotel_name: ${hotel_name}`);
        console.log(`room_name: ${room_name}`);
        console.log(`room_price: ${room_price}`);
        console.log(`number_of_beds: ${number_of_beds}`);
        console.log(`room_type: ${room_type}`);
        console.log(`checkin: ${checkin}`);
        console.log(`checkout: ${checkout}`);
        console.log(`adult: ${adult}`);
        console.log(`children: ${children}`);


        $.ajax({
            url:'/booking/add_to_selection/',
            data: {
                'id': id,
                'hotel_id': hotel_id,
                'hotel_name': hotel_name,
                'room_number': room_number,
                'room_name': room_name,
                'room_price': room_price,
                'number_of_beds': number_of_beds,
                'room_type': room_type,
                'room_id': room_id,
                'checkin': checkin,
                'checkout': checkout,
                'adult': adult,
                'children': children,
            },
            dataType: 'json',
            beforeSend: function(){
                console.log("Adding room...");
                button.html("<i class='fa fa-clock-rotate-left'></i> Adding room... ")
            },
            success: function(response){
                button.html("<i class='fa fa-check-circle'></i> Added To Selection ")

                console.log("Added Room To Selection!");
                $(".room-count").text(response.total_selected_items)
                
                const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 1000,
                    timerProgressBar: true,
                })
                    
                Toast.fire({
                    icon: 'success',
                    title: 'Added Room To Selection!'
                })
            }
        })

    })

    
})

// Delete Items From Cart
$(document).on("click", ".delete-item", function() {
    let id = $(this).attr("data-item")
    let button = $(this)

    Swal.fire({
        title: "Are you sure you want to delete this room?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, Delete it!"
    }).then((result)=> {
        if(result.isConfirmed){
            $.ajax({
                url: "/booking/delete_selection/",
                data: {
                    "id": id
                },
                dataType: "json",
                beforeSend: function() {
                    button.html("<i class='fas fa-spinner fa-spin></i>")
                },
                success: function(res){
                    console.log(res.total_selected_item);
                    $(".room-count").text(res.total_selected_item)
                    $(".selection-list").html(res.data)
                }
            })
        }
    })


    function makeAjaxCall() {
        $.ajax({
            url: "/update_room_status/",
            type: "GET",
            success: function(data) {
                console.log("Checked Rooms");
            },
        })
    }
    
    // setInterval(makeAjaxCall, 3000);
    setInterval(makeAjaxCall,86400000);
    
    
})







