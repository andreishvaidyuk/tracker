var socket = io.connect('http://' + document.domain + ':' + location.port);

      socket.on( 'connect', function() {
        socket.emit( 'message', {
          data: 'User Connected'
        } )
        var form = $( 'form' ).on( 'submit', function( e ) {
          e.preventDefault()
          let sat_name = $( 'input.satname' ).val()
          socket.emit( 'my event', {
            satellite_name : sat_name,
          } )
          $( 'input.message' ).val( '' ).focus()
        } )
      } )

        socket.on( 'connect', function() {
            socket.emit( 'message', {
                data: 'User Connected'
            } )
            var form = $( 'form' ).on( 'submit', function( e ) {
                e.preventDefault()
                let sat_name = $( 'input.satname' ).val()
                socket.emit( 'start', {
                    satellite_name : sat_name,
                } )
                $( 'input.message' ).val( '' ).focus()
            } )
        var form = $('form').on('submit', function(e){
            socket.emit('stop', {

            })
        })
        } )

      socket.on( 'my response', function( msg ) {
        console.log( msg )
        var obj = JSON.parse(msg)
        if( typeof obj.Name !== 'undefined' )
        {

//            $('#table').tabulator({
//                columns:[
//                    {title:"Column1", field:"column1"},
//                    {title:"Column2", field:"column2"},
//                ],
//            });
//
//            var sampleData= [
//                {id:1, name:"Oli Bob"},
//                {id:2, name:"Mary May"},
//                {id:3, name:"Christine Lobowski"},
//                {id:4, name:"Brendon Philips"},
//                {id:5, name:"Margret Marmajuke"},
//            ]
//
//            $("#table").tabulator("setData", sampleData);
//
//            $(window).resize(function(){
//                $("#table").tabulator("redraw");
//            });
          $( 'table.table' ).append( '<p>'+obj.Time+'</p>' )
          $( 'table.table' ).append( '<p>'+obj.Latitude+'</p>' )
          $( 'table.table' ).append( '<p>'+obj.Longitude+'</p>' )
          $( 'table.table' ).append( '<p>'+obj.Altitude+'</p>' )
          $( 'table.table' ).append( '<p>'+obj.Azimuth+'</p>' )
          $( 'table.table' ).append( '<p>'+obj.Geocentric_height+'</p>' )
          $( 'table.table' ).append( '<p>'+obj.Shadow+'</p>' )
        }
      })