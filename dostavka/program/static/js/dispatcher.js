// dispatcher.js (обновленный)
$(document).ready(function() {
    // Инициализация автозаполнения
    $('#clientSearch').autocomplete({
        source: '/client-autocomplete/',
        select: function(event, ui) {
            $('#clientInfo').html(`
                <p class="mb-1"><strong>Имя:</strong> ${ui.item.name}</p>
                <p class="mb-0"><strong>Адрес:</strong> ${ui.item.address}</p>
            `);
            $('<input>').attr({
                type: 'hidden',
                name: 'client_id',
                value: ui.item.id
            }).appendTo('form');
        }
    });

    // Инициализация popover
    $('[data-toggle="popover"]').popover({
        placement: 'auto',
        trigger: 'hover',
        html: true,
        sanitize: false
    });

    // Динамическое добавление блюд
    $('#addDishBtn').click(function() {
        const newRow = `
        <div class="dish-row mb-2 d-flex align-items-center gap-2">
            <select name="dishes" class="form-select" required>
                {% for dish in today_menu.dishes.all %}
                <option value="{{ dish.id }}" data-price="{{ dish.price }}">
                    {{ dish.name }} ({{ dish.price }}₽)
                </option>
                {% endfor %}
            </select>
            <input type="number" name="quantities" class="form-control" min="1" value="1" style="width: 80px;">
            <button type="button" class="btn btn-danger btn-sm remove-dish">&times;</button>
        </div>`;
        $('#dishesContainer').append(newRow);
        updateTotal();
    });

    // Удаление блюда
    $(document).on('click', '.remove-dish', function() {
        $(this).closest('.dish-row').remove();
        updateTotal();
    });

    // Расчет стоимости
    function updateTotal() {
        let total = 0;
        $('.dish-row').each(function() {
            const price = $(this).find('option:selected').data('price');
            const quantity = $(this).find('input').val();
            total += price * quantity;
        });
        $('#totalPrice').text(total + '₽');
    }

    $(document).on('change', 'select, input', updateTotal);
});