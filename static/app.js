let lezioni = [];
let filteredLezioni = [];
let selectedFile = null;
let currentView = 'cube';
let carouselPosition = 0;
let expandedCubeId = null;

const today = new Date().toISOString().split('T')[0];
const mesiItaliani = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 
                     'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'];

document.addEventListener('DOMContentLoaded', () => {
    loadLezioni();
    loadStats();
    setupDragDrop();
    
    document.getElementById('data').addEventListener('change', (e) => {
        const date = new Date(e.target.value);
        const giorni = ['Domenica', 'Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato'];
        document.getElementById('giorno').value = giorni[date.getDay()];
    });
});

function setView(view) {
    currentView = view;
    document.getElementById('viewCube').classList.toggle('active', view === 'cube');
    document.getElementById('viewList').classList.toggle('active', view === 'list');
    document.getElementById('carouselView').style.display = view === 'cube' ? 'block' : 'none';
    document.getElementById('tableView').style.display = view === 'list' ? 'block' : 'none';
    
    if (view === 'cube') {
        renderCarousel();
    } else {
        renderTable();
    }
}

async function loadLezioni() {
    try {
        const response = await fetch('/api/lezioni');
        lezioni = await response.json();
        applyFilters();
    } catch (error) {
        showToast('Errore nel caricamento', 'error');
    }
}

async function loadStats() {
    try {
        const response = await fetch('/api/stats');
        const stats = await response.json();
        document.getElementById('statTotale').textContent = stats.totale_lezioni;
        document.getElementById('statPresenze').textContent = stats.presenze;
        document.getElementById('statAssenze').textContent = stats.assenze;
        document.getElementById('statPercentuale').textContent = stats.percentuale_presenza + '%';
        document.getElementById('statOrePresenti').textContent = stats.ore_presenti;
        document.getElementById('statOreTotali').textContent = stats.ore_totali;
    } catch (error) {
        console.error('Errore stats:', error);
    }
}

function applyFilters() {
    const search = document.getElementById('searchInput').value.toLowerCase();
    const presenza = document.getElementById('filterPresenza').value;
    const mese = document.getElementById('filterMese').value;
    
    filteredLezioni = lezioni.filter(l => {
        const matchSearch = !search || 
            (l.nome_lezione && l.nome_lezione.toLowerCase().includes(search)) ||
            (l.professore && l.professore.toLowerCase().includes(search)) ||
            (l.aula && l.aula.toLowerCase().includes(search));
        
        const matchPresenza = !presenza || 
            (presenza === 'presente' && l.presente && !l.assenza_da) ||
            (presenza === 'assente' && !l.presente && !l.assenza_da) ||
            (presenza === 'parziale' && l.assenza_da);
        
        const matchMese = !mese || (l.data && l.data.startsWith(mese));
        
        return matchSearch && matchPresenza && matchMese;
    });
    
    if (currentView === 'cube') {
        renderCarousel();
    } else {
        renderTable();
    }
}

function renderCarousel() {
    const track = document.getElementById('carouselTrack');
    
    const byDate = {};
    filteredLezioni.forEach(l => {
        if (!byDate[l.data]) byDate[l.data] = [];
        byDate[l.data].push(l);
    });
    
    const dates = Object.keys(byDate).sort();
    
    if (dates.length === 0) {
        track.innerHTML = '<div class="empty-state"><div class="empty-state-icon">📚</div><h3>Nessuna lezione</h3></div>';
        return;
    }
    
    let todayIndex = dates.findIndex(d => d === today);
    if (todayIndex === -1) {
        todayIndex = dates.findIndex(d => d >= today);
        if (todayIndex === -1) todayIndex = dates.length - 1;
    }
    
    track.innerHTML = dates.map(date => {
        const lessons = byDate[date];
        const dateObj = new Date(date);
        const dayNum = dateObj.getDate();
        const dayName = ['Dom', 'Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab'][dateObj.getDay()];
        const month = mesiItaliani[dateObj.getMonth()];
        const isToday = date === today;
        
        let status = 'assente';
        const hasPresente = lessons.some(l => l.presente && !l.assenza_da);
        const hasAssente = lessons.some(l => !l.presente && !l.assenza_da);
        const hasParziale = lessons.some(l => l.assenza_da);
        
        if (hasPresente && !hasAssente && !hasParziale) status = 'presente';
        else if (hasParziale) status = 'parziale';
        else if (hasPresente && hasAssente) status = 'mixed';
        
        return `
            <div class="day-cube ${isToday ? 'today' : ''}" data-date="${date}" onclick="expandCube('${date}')">
                <div class="cube-status ${status}"></div>
                <div class="cube-compact-content">
                    <div class="cube-day-name">${dayName}</div>
                    <div class="cube-date">${dayNum}</div>
                    <div class="cube-month">${month}</div>
                    <div class="cube-lessons">${lessons.length} ${lessons.length === 1 ? 'lezione' : 'lezioni'}</div>
                </div>
            </div>
        `;
    }).join('');
    
    carouselPosition = -todayIndex * 220 + 200;
    updateCarouselPosition();
}

function renderLessonCard(l) {
    let statusClass = l.presente ? 'presente' : 'assente';
    let statusText = l.presente ? '✓ Presente' : '✗ Assente';
    
    if (l.assenza_da) {
        statusClass = 'parziale';
        statusText = `⏱ Assente ${l.assenza_da} - ${l.assenza_a}`;
    }
    
    return `
        <div class="lesson-card ${statusClass}">
            <div class="lesson-card-header">
                <div>
                    <h4>${l.nome_lezione || 'Lezione'}</h4>
                    <div class="lesson-meta">${l.professore || '-'} • ${l.aula || '-'}</div>
                </div>
                <span class="lesson-time">${l.orario_inizio || '-'} - ${l.orario_fine || '-'}</span>
            </div>
            <div class="presence-selector">
                <button class="btn btn-sm ${statusClass === 'presente' ? 'btn-success' : ''}" 
                        onclick="event.stopPropagation(); openPresenzaModal(${l.id})"
                        style="${statusClass !== 'presente' ? 'background: #eee; color: #666;' : ''}">
                    ${statusText} - Modifica
                </button>
                <button class="btn btn-sm" onclick="event.stopPropagation(); openEditModal(${l.id})" 
                        style="background: #e3f2fd; color: #1976d2; margin-left: 5px;">
                    ✏️ Modifica
                </button>
            </div>
        </div>
    `;
}

function expandCube(date) {
    const lessons = filteredLezioni.filter(l => l.data === date);
    if (lessons.length === 0) return;
    
    const dateObj = new Date(date);
    const dayName = ['Domenica', 'Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato'][dateObj.getDay()];
    const dayNum = dateObj.getDate();
    const month = mesiItaliani[dateObj.getMonth()];
    
    const modal = document.getElementById('cubeDetailsModal');
    const title = document.getElementById('cubeDetailsTitle');
    const content = document.getElementById('cubeDetailsContent');
    
    title.innerHTML = `${dayName} ${dayNum} ${month} ${dateObj.getFullYear()}`;
    content.innerHTML = lessons.map(l => renderLessonCard(l)).join('');
    
    modal.classList.add('active');
    document.getElementById('cubeOverlay').classList.add('active');
}

function closeExpandedCube() {
    document.getElementById('cubeDetailsModal').classList.remove('active');
    document.getElementById('cubeOverlay').classList.remove('active');
}

function carouselPrev() {
    carouselPosition += 220;
    if (carouselPosition > 200) carouselPosition = 200;
    updateCarouselPosition();
}

function carouselNext() {
    const track = document.getElementById('carouselTrack');
    const maxScroll = -(track.children.length * 220 - window.innerWidth + 200);
    carouselPosition -= 220;
    if (carouselPosition < maxScroll) carouselPosition = maxScroll;
    updateCarouselPosition();
}

function updateCarouselPosition() {
    document.getElementById('carouselTrack').style.transform = `translateX(${carouselPosition}px)`;
}

function renderTable() {
    const tbody = document.getElementById('lezioniBody');
    const emptyState = document.getElementById('emptyState');
    const table = document.getElementById('lezioniTable');
    
    if (filteredLezioni.length === 0) {
        table.style.display = 'none';
        emptyState.style.display = 'block';
        return;
    }
    
    table.style.display = 'table';
    emptyState.style.display = 'none';
    
    tbody.innerHTML = filteredLezioni.map(l => {
        let statusClass = l.presente ? 'presente' : 'assente';
        let statusText = l.presente ? '✓ Presente' : '✗ Assente';
        
        if (l.assenza_da) {
            statusClass = 'parziale';
            statusText = `⏱ ${l.assenza_da}-${l.assenza_a}`;
        }
        
        return `
            <tr>
                <td>${l.giorno || '-'}</td>
                <td>${formatDate(l.data)}</td>
                <td>${l.aula || '-'}</td>
                <td>${l.orario_inizio || '-'} - ${l.orario_fine || '-'}</td>
                <td>${l.totale_ore || '-'}</td>
                <td><strong>${l.nome_lezione || '-'}</strong></td>
                <td>${l.professore || '-'}</td>
                <td>
                    <button class="presenza-btn ${statusClass}" onclick="openPresenzaModal(${l.id})">
                        ${statusText}
                    </button>
                </td>
                <td class="actions-cell">
                    <button class="btn-icon edit" onclick="openEditModal(${l.id})" title="Modifica">✏️</button>
                    <button class="btn-icon delete" onclick="deleteLezione(${l.id})" title="Elimina">🗑️</button>
                </td>
            </tr>
        `;
    }).join('');
}

function formatDate(dateStr) {
    if (!dateStr) return '-';
    try {
        const [year, month, day] = dateStr.split('-');
        return `${day}/${month}/${year}`;
    } catch {
        return dateStr;
    }
}

function openPresenzaModal(id) {
    const lezione = lezioni.find(l => l.id === id);
    if (!lezione) return;
    
    document.getElementById('presenzaLezioneId').value = id;
    document.getElementById('presenzaOrarioInizio').value = lezione.orario_inizio || '';
    document.getElementById('presenzaOrarioFine').value = lezione.orario_fine || '';
    document.getElementById('presenzaLessonInfo').innerHTML = `
        <strong>${lezione.nome_lezione || 'Lezione'}</strong><br>
        <span style="color: #666;">${lezione.professore || '-'} • ${formatDate(lezione.data)} • ${lezione.orario_inizio}-${lezione.orario_fine}</span>
    `;
    
    document.querySelectorAll('.presence-option').forEach(el => el.classList.remove('selected'));
    document.getElementById('partialTimeInputs').classList.remove('active');
    document.getElementById('assenzaDa').value = lezione.orario_inizio || '';
    document.getElementById('assenzaA').value = lezione.orario_fine || '';
    
    if (lezione.assenza_da) {
        selectPresenceOption('assente-partial');
        document.getElementById('assenzaDa').value = lezione.assenza_da;
        document.getElementById('assenzaA').value = lezione.assenza_a;
    } else if (lezione.presente) {
        selectPresenceOption('presente');
    } else {
        selectPresenceOption('assente-full');
    }
    
    document.getElementById('presenzaModal').classList.add('active');
}

function closePresenzaModal() {
    document.getElementById('presenzaModal').classList.remove('active');
}

function selectPresenceOption(type) {
    document.querySelectorAll('.presence-option').forEach(el => {
        el.classList.remove('selected', 'presente', 'assente-full', 'assente-partial');
    });
    
    const option = document.querySelector(`.presence-option input[value="${type}"]`);
    if (option) {
        option.checked = true;
        option.closest('.presence-option').classList.add('selected', type);
    }
    
    document.getElementById('partialTimeInputs').classList.toggle('active', type === 'assente-partial');
}

async function savePresenza() {
    const id = document.getElementById('presenzaLezioneId').value;
    const type = document.querySelector('input[name="presenzaType"]:checked')?.value;
    
    let data = { presente: false, assenza_da: null, assenza_a: null };
    
    if (type === 'presente') {
        data.presente = true;
    } else if (type === 'assente-partial') {
        data.assenza_da = document.getElementById('assenzaDa').value;
        data.assenza_a = document.getElementById('assenzaA').value;
    }
    
    try {
        await fetch(`/api/lezioni/${id}/presenza`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        showToast('Presenza aggiornata!', 'success');
        closePresenzaModal();
        closeExpandedCube();
        await loadLezioni();
        await loadStats();
    } catch (error) {
        showToast('Errore nell\'aggiornamento', 'error');
    }
}

function openAddModal() {
    document.getElementById('modalTitle').textContent = 'Nuova Lezione';
    document.getElementById('lezioneForm').reset();
    document.getElementById('lezioneId').value = '';
    document.getElementById('lezioneModal').classList.add('active');
}

function openEditModal(id) {
    const lezione = lezioni.find(l => l.id === id);
    if (!lezione) return;
    
    document.getElementById('modalTitle').textContent = 'Modifica Lezione';
    document.getElementById('lezioneId').value = id;
    document.getElementById('giorno').value = lezione.giorno || '';
    document.getElementById('data').value = lezione.data || '';
    document.getElementById('aula').value = lezione.aula || '';
    document.getElementById('orarioInizio').value = lezione.orario_inizio || '';
    document.getElementById('orarioFine').value = lezione.orario_fine || '';
    document.getElementById('totaleOre').value = lezione.totale_ore || '';
    document.getElementById('nomeLezione').value = lezione.nome_lezione || '';
    document.getElementById('professore').value = lezione.professore || '';
    document.getElementById('note').value = lezione.note || '';
    
    document.getElementById('lezioneModal').classList.add('active');
}

function closeModal() {
    document.getElementById('lezioneModal').classList.remove('active');
}

async function saveLezione() {
    const id = document.getElementById('lezioneId').value;
    const data = {
        giorno: document.getElementById('giorno').value,
        data: document.getElementById('data').value,
        aula: document.getElementById('aula').value,
        orario_inizio: document.getElementById('orarioInizio').value,
        orario_fine: document.getElementById('orarioFine').value,
        totale_ore: document.getElementById('totaleOre').value || null,
        nome_lezione: document.getElementById('nomeLezione').value,
        professore: document.getElementById('professore').value,
        note: document.getElementById('note').value
    };
    
    try {
        if (id) {
            await fetch(`/api/lezioni/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            showToast('Lezione aggiornata!', 'success');
        } else {
            await fetch('/api/lezioni', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            showToast('Lezione aggiunta!', 'success');
        }
        
        closeModal();
        closeExpandedCube();
        await loadLezioni();
        await loadStats();
    } catch (error) {
        showToast('Errore nel salvataggio', 'error');
    }
}

async function deleteLezione(id) {
    if (!confirm('Sei sicuro di voler eliminare questa lezione?')) return;
    
    try {
        await fetch(`/api/lezioni/${id}`, { method: 'DELETE' });
        showToast('Lezione eliminata', 'info');
        closeExpandedCube();
        await loadLezioni();
        await loadStats();
    } catch (error) {
        showToast('Errore nell\'eliminazione', 'error');
    }
}

function openImportModal() {
    selectedFile = null;
    document.getElementById('csvFile').value = '';
    document.getElementById('importBtn').disabled = true;
    document.getElementById('importModal').classList.add('active');
}

function closeImportModal() {
    document.getElementById('importModal').classList.remove('active');
}

function handleFileSelect(event) {
    selectedFile = event.target.files[0];
    if (selectedFile) {
        document.getElementById('importBtn').disabled = false;
    }
}

function setupDragDrop() {
    const zone = document.getElementById('importZone');
    
    zone.addEventListener('dragover', (e) => {
        e.preventDefault();
        zone.classList.add('dragover');
    });
    
    zone.addEventListener('dragleave', () => {
        zone.classList.remove('dragover');
    });
    
    zone.addEventListener('drop', (e) => {
        e.preventDefault();
        zone.classList.remove('dragover');
        if (e.dataTransfer.files.length) {
            selectedFile = e.dataTransfer.files[0];
            document.getElementById('importBtn').disabled = false;
        }
    });
}

async function uploadCSV() {
    if (!selectedFile) return;
    
    const formData = new FormData();
    formData.append('file', selectedFile);
    
    try {
        const response = await fetch('/api/import-csv', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            showToast(`Importate ${result.imported} lezioni!`, 'success');
            closeImportModal();
            await loadLezioni();
            await loadStats();
        } else {
            showToast('Errore: ' + result.error, 'error');
        }
    } catch (error) {
        showToast('Errore nell\'importazione', 'error');
    }
}

function exportCSV() {
    window.location.href = '/api/export-csv';
    showToast('Download avviato!', 'success');
}

function showToast(message, type = 'info') {
    const existing = document.querySelector('.toast');
    if (existing) existing.remove();
    
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => toast.remove(), 3000);
}
