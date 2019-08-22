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
      socket.on( 'my response', function( msg ) {
        console.log( msg )
        var obj = JSON.parse(msg)
        if( typeof obj.Name !== 'undefined' )
        {
          $( 'div.table' ).append( '<div>'+obj.Time+'</div>' )
          $( 'div.table' ).append( '<div>'+obj.Latitude+'</div>' )
          $( 'div.table' ).append( '<div>'+obj.Longitude+'</div>' )
          $( 'div.table' ).append( '<div>'+obj.Altitude+'</div>' )
          $( 'div.table' ).append( '<div>'+obj.Azimuth+'</div>' )
          $( 'div.table' ).append( '<div>'+obj.Geocentric_height+'</div>' )
          $( 'div.table' ).append( '<div>'+obj.Distance+'</div>' )
          $( 'div.table' ).append( '<div>'+obj.Range_rate+'</div>' )
          $( 'div.table' ).append( '<div>'+obj.Shadow+'</div>' )
        }
      })