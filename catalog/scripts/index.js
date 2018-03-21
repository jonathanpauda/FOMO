$(function(context) {
  return function(){
    console.log(context)
    var container = $('#catalog_container')
    container.load('/catalog/index.products/' + context.cat_id + "/" + context.pnum)
    num_pages = parseInt(context.num_pages)

    $('#previous_page').click(function(){
      console.log('prev')
      var pageNumber = $('#page_number').text()
      if(pageNumber>1){
        pageNumber--
        $('#page_number').text(pageNumber)
        console.log(pageNumber)
      }
      $('#catalog_container').load('/catalog/index.products/' + context.cat_id + '/' + pageNumber)
    })

    $('#next_page').click(function(){
      console.log('next')
      var pageNumber = $('#page_number').text()
      if(pageNumber<num_pages){
        pageNumber++
        $('#page_number').text(pageNumber)
        console.log(pageNumber)
      }
      $('#catalog_container').load('/catalog/index.products/' + context.cat_id + '/' + pageNumber)
    })
  }
}(DMP_CONTEXT.get()))
