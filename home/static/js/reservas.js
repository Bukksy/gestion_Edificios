document.addEventListener("DOMContentLoaded", function () {
    const reserveButton = document.getElementById("reserveButton");
    const calendarDays = document.getElementById("calendarDays");
    const monthYear = document.getElementById("monthYear");
    const prevMonth = document.getElementById("prevMonth");
    const nextMonth = document.getElementById("nextMonth");
    const showCalendarBtn = document.getElementById("showCalendarBtn");
    const reservaSelect = document.getElementById("reservaSelect");

    let selectedDay = null;
    let currentDate = new Date();
    let currentMonth = currentDate.getMonth();
    let currentYear = currentDate.getFullYear();
    let selectedReserva = null;

    const reservedDays = {
        sala_reuniones: new Set(),
        cancha_tenis: new Set(),
        piscina: new Set()
    };

    function updateCalendar() {
        const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
        monthYear.textContent = `${monthNames[currentMonth]} ${currentYear}`;

        calendarDays.innerHTML = "";

        const firstDay = new Date(currentYear, currentMonth, 1).getDay();
        const lastDate = new Date(currentYear, currentMonth + 1, 0).getDate();

        for (let i = 0; i < firstDay; i++) {
            const emptyDay = document.createElement("div");
            calendarDays.appendChild(emptyDay);
        }

        for (let day = 1; day <= lastDate; day++) {
            const dayElement = document.createElement("div");
            dayElement.classList.add("calendar-day");
            dayElement.textContent = day;

            const currentDay = new Date();
            if (day === currentDay.getDate() && currentMonth === currentDay.getMonth() && currentYear === currentDay.getFullYear()) {
                dayElement.classList.add("current");
            }

            if (new Date(currentYear, currentMonth, day) < currentDate) {
                dayElement.classList.add("disabled");
            }

            if (reservedDays[selectedReserva].has(day)) {
                dayElement.classList.add("disabled");
            }

            dayElement.addEventListener("click", function () {
                if (dayElement.classList.contains("disabled")) return;

                if (selectedDay) {
                    selectedDay.classList.remove("selected");
                }

                dayElement.classList.add("selected");
                selectedDay = dayElement;

                reserveButton.disabled = false;
            });

            calendarDays.appendChild(dayElement);
        }
    }

    reservaSelect.addEventListener("change", function () {
        selectedReserva = reservaSelect.value;
        showCalendarBtn.disabled = false;
        updateCalendar();
    });

    prevMonth.addEventListener("click", function () {
        currentMonth--;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        }
        updateCalendar();
    });

    nextMonth.addEventListener("click", function () {
        currentMonth++;
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        updateCalendar();
    });

    reserveButton.addEventListener("click", function () {
        if (selectedDay) {
            Swal.fire({
                title: '¡Reserva Confirmada!',
                text: `Has reservado el día ${selectedDay.textContent} para ${selectedReserva}`,
                icon: 'success',
                confirmButtonText: 'Ok'
            }).then(function () {
                reservedDays[selectedReserva].add(Number(selectedDay.textContent));
                updateCalendar();
                selectedDay.classList.remove("selected");
                selectedDay = null;
                reserveButton.disabled = true;
            });
        }
    });
});