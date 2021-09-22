<template>
  <div>
    <center>
      <div class='card'>
        <br>
        <div class='grid grid-cols-7'>
          <div class='col-start-3 row-start-2'>
            <span class='px-2 py-2'>Телефон</span>
          </div>
          <div class='col-start-4 row-start-2'>
            <div style='width : 1px; height : 30px; background : #EBD2DA'></div>
          </div>
          <nuxt-link to="/pnr" class='col-start-5 row-start-2'>
            <div>
              <span class='active-turner px-4 py-2'>PNR</span>
            </div>
          </nuxt-link>
        </div>

        <br><br>
        <input placeholder="Ваш номер телефона" class='text-field' ref = 'cellPhoneTextField' type = 'tel'/>
        <br><br>

        <nuxt-link to ='/' style = 'position:relative; float : right; right : 80px'>
            <span class = 'active-turner px-4 py-2'>Далее</span>
        </nuxt-link>

        <br><br>

        <div class='grid'>
          <div class='row-start-1'><br></div>
          <div class='row-start-2'><br></div>
          <div class='row-start-3'><br></div>
          <div class='row-start-4'><br></div>
          <div class=' row-start-5'><br></div>
          <div class='row-start-6'><br></div>
          <div class=' row-start-7'><br></div>
          <div class='row-start-8'><br></div>
          <div class='row-start-9'><br></div>
          <div class='row-start-10'>
             <span>
              Есть вопросы?
            </span>
          </div>
          <div class='row-start-11'>
            <span class = 'active-turner px-2 py-1'>
              helpdesk@radolyn.com
            </span>
          </div>
        </div>
      </div>
    </center>
  </div>

</template>

<script>

import IMask from "imask";

export default {
  data() {
    return {}
  },
  mounted() {
    const textFieldMaskOptions = {
      mask: '+{7}(000)000-00-00'
    }
    IMask(this.$refs.cellPhoneTextField, textFieldMaskOptions)
  }
}

</script>

<style src='../layouts/default.css'></style>
<style>

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
