var socket = io.connect('http://' + document.domain + ':' + location.port);
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
      } )
      socket.on( 'my response', function( msg ) {
        console.log( msg )
        var obj = JSON.parse(msg)
        if( typeof obj.Name !== 'undefined' )
        {


          $( '.date' ).text(obj.Time)
          $( '.latitude' ).text(obj.Latitude)
          $( '.longitude' ).text(obj.Longitude)
          $( '.altitude' ).text(obj.Altitude)
          $( '.azimuth' ).text(obj.Azimuth)
          $( '.height' ).text(obj.Geocentric_height)
          $( '.inShadow' ).text(obj.Shadow)
        }
      })