<template>
  <div>
    <center>
      <div class='card'>
        <br>
        <div class='grid grid-cols-7'>
          <nuxt-link to="/cellphone" class='col-start-3 row-start-2'>
            <div>
              <span class='active-turner px-2 py-2'>Телефон</span>
            </div>
          </nuxt-link>
          <div class='col-start-4 row-start-2'>
            <div style='width : 1px; height : 30px; background : #EBD2DA'></div>
          </div>
          <div class='col-start-5 row-start-2'>
            <div>
              <span class='px-4 py-2'>PNR</span>
            </div>
            <img src='../static/ellipse.png' class='pnr-quest' @click='pnrShow = true'>
          </div>
        </div>
        <div v-show='pnrShow' style='border : 1px solid #EBD2DA; border-radius: 10px; width : 420px'>
          <span>
            PNR - запись в базе данных компьютерной системы бронирования о маршруте пассажира, находящаяся на посадочном талоне
          </span>
        </div>

        <br>
        <input placeholder="Ваш PNR" class='text-field' style = 'width : 380px; height : 60px;' type = 'tel'/>

        <br><br>

        <nuxt-link to ='/' style = 'position:relative; float : right; right : 80px'>
          <span class = 'active-turner px-4 py-2'>Далее</span>
        </nuxt-link>

      </div>
    </center>
  </div>

</template>

<script>

export default {
  data() {
    return {
      pnrShow: false
    }
  },
}

</script>

<style src='../layouts/default.css'></style>
<style>

.pnr-quest {
  position: relative;
  left: 15px;
  bottom: 24px;
  float: right;
  cursor: pointer;
}

.card {
  position: relative;
  top: 40px;
  background-color: #403939;
  height: 520px;
  max-width: 540px;
  border-radius: 10px;
  box-shadow: 8px 8px 5px #574D4D;
}

.card span {
  font-weight: 500 !important;
  color: #EBD2DA;
  font-size: 17px;
}

</style>
