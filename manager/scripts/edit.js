$('#type').on('change', function(){
  if($('#type').val()=='BulkProduct'){
    $('.bulk-product').closest('p').show(2000)
    $('.individual-product').closest('p').hide(2000)
    $('.rental-product').closest('p').hide(2000)
    $('.not-bulk-product').closest('p').hide(2000)
  }
  else if($('#type').val()=='IndividualProduct'){
    $('.bulk-product').closest('p').hide(2000)
    $('.individual-product').closest('p').show(2000)
    $('.not-bulk-product').closest('p').show(2000)
    $('.rental-product').closest('p').hide(2000)
  }
  else{
    $('.bulk-product').closest('p').hide(2000)
    $('.individual-product').closest('p').hide(2000)
    $('.not-bulk-product').show(2000)
    $('.rental-product').closest('p').show(2000)
  }
})

$(document).ready(function(){
  if($('#type').val()=='BulkProduct'){
    $('.bulk-product').closest('p').show(2000)
    $('.individual-product').closest('p').hide(2000)
    $('.rental-product').closest('p').hide(2000)
    $('.not-bulk-product').closest('p').hide(2000)
  }
  else if($('#type').val()=='IndividualProduct'){
    $('.bulk-product').closest('p').hide(2000)
    $('.individual-product').closest('p').show(2000)
    $('.not-bulk-product').closest('p').show(2000)
    $('.rental-product').closest('p').hide(2000)
  }
  else{
    $('.bulk-product').closest('p').hide(2000)
    $('.individual-product').closest('p').hide(2000)
    $('.not-bulk-product').show(2000)
    $('.rental-product').closest('p').show(2000)
  }
});
