// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching: true,
    bInfo: true,
    bSort: true,
    dom: 'lBfrtip',
    buttons: [
      {
        extend: 'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-info',
        titleAttr: 'Copy'
      },
      {
        extend: 'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-info',
        titleAttr: 'Export XLS'
      },
      {
        extend: 'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-info',
        titleAttr: 'Export PDF'
      }
    ]
  });
  
});
