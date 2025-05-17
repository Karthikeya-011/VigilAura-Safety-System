document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const sosBtn = document.getElementById('sosBtn');
    const fakeCallBtn = document.getElementById('fakeCallBtn');
    const locationBtn = document.getElementById('locationBtn');
    const alertSound = document.getElementById('alertSound');
    const fakeCallSound = document.getElementById('fakeCallSound');
    
    // SOS Alert
    sosBtn.addEventListener('click', async () => {
        const statusEl = document.getElementById('sosStatus');
        statusEl.textContent = "Sending emergency alert...";
        statusEl.style.color = "var(--primary)";
        
        try {
            // Play alert sound
            alertSound.play();
            
            // Send alert to server
            const response = await fetch('/trigger_alert', {
                method: 'POST'
            });
            const data = await response.json();
            
            statusEl.textContent = data.status;
            statusEl.style.color = "var(--success)";
        } catch (error) {
            statusEl.textContent = `Error: ${error.message}`;
            statusEl.style.color = "var(--primary)";
        }
    });
    
    // Fake Call
    fakeCallBtn.addEventListener('click', async () => {
        const statusEl = document.getElementById('fakeCallStatus');
        statusEl.textContent = "Playing fake call...";
        statusEl.style.color = "var(--accent)";
        
        try {
            // Play fake call sound
            fakeCallSound.play();
            
            // Notify server
            const response = await fetch('/fake_call', {
                method: 'POST'
            });
            const data = await response.json();
            
            statusEl.textContent = data.status;
            statusEl.style.color = "var(--success)";
        } catch (error) {
            statusEl.textContent = `Error: ${error.message}`;
            statusEl.style.color = "var(--accent)";
        }
    });
    
    // Location Sharing
    locationBtn.addEventListener('click', async () => {
        const statusEl = document.getElementById('locationStatus');
        statusEl.textContent = "Getting your location...";
        statusEl.style.color = "var(--secondary)";
        
        try {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    async (position) => {
                        const locationData = {
                            lat: position.coords.latitude,
                            lon: position.coords.longitude
                        };
                        
                        // Send to server
                        const response = await fetch('/get_location', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify(locationData)
                        });
                        const data = await response.json();
                        
                        statusEl.textContent = `${data.status} (Lat: ${locationData.lat.toFixed(4)}, Lon: ${locationData.lon.toFixed(4)})`;
                        statusEl.style.color = "var(--success)";
                    },
                    (error) => {
                        statusEl.textContent = `Location error: ${error.message}`;
                        statusEl.style.color = "var(--secondary)";
                    }
                );
            } else {
                statusEl.textContent = "Geolocation not supported";
                statusEl.style.color = "var(--secondary)";
            }
        } catch (error) {
            statusEl.textContent = `Error: ${error.message}`;
            statusEl.style.color = "var(--secondary)";
        }
    });
});