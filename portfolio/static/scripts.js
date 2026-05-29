
        function updateTime() {
            const now = new Date();
            const timeString = now.toLocaleTimeString();
            document.getElementById("time").innerText = timeString;
        }

        // Update every second
        setInterval(updateTime, 1000);

        // Run immediately
        updateTime();

    const text1 = "Design that";
    const text2 = "INSPIRES";
    const text3 = "People";

    function typeText(element, text, speed, callback) {
        let i = 0;

        function typing() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(typing, speed);
            } else {
                if (callback) callback();
            }
        }

        typing();
    }

    const el1 = document.getElementById("t1");
    const el2 = document.getElementById("t2");
    const el3 = document.getElementById("t3");

    // Step 1
    typeText(el1, text1, 100, () => {

        // Step 2
        setTimeout(() => {
            typeText(el2, text2, 100, () => {

                // Step 3
                setTimeout(() => {
                    typeText(el3, text3, 100);
                }, 500);

            });
        }, 300);

    });


        
