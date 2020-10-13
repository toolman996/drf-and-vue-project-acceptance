<template>
    <div class="cart_item">
        <div class="cart_column column_1">
            <el-checkbox class="my_el_checkbox" v-model="value.selected"></el-checkbox>
        </div>
        <div class="cart_column column_2">
            <img :src="value.course_img" alt="">
            <span><router-link :to="'/course/'+value.id">{{value.name}}</router-link></span>
        </div>
        <div class="cart_column column_3">
            <el-select  v-model="value.expire_id" size="mini" placeholder="请选择购买有效期" class="my_el_select">
                <el-option :label="msg_time.mfg_text" :value="msg_time.id" v-for="(msg_time,index) in value.mfg" :key="index"></el-option>
            </el-select>
        </div>
        <div class="cart_column column_4">{{value.true_price.toFixed(2)}}</div>
        <div class="cart_column column_4"><a href="javascript:" @click="del">删除</a></div>
    </div>
</template>

<script>
    export default {
        name: "CartItem",
        //父传子props属性
        props:['value'],
        //监听事件
        watch:{
            //如果复选框状态发生改变执行以下函数
            "value.selected":function () {
                this.change_status()
            },
            'value.expire_id':function () {
                this.mfg_status()
            }
        },
        methods:{
            //切换有效期状态
            mfg_status(){
                let token = localStorage.user_token || sessionStorage.user_token
                this.$axios({
                    url: this.$settings.HOST+'shoppingcart/option/',
                    method:'put',
                    data:{
                        course_id:this.value.id,
                        mfg_id:this.value.expire_id
                    },
                    headers:{
                        'Authorization': 'jwt '+token
                    }

                }).then(success=>{
                    this.$message.success(success.data.message)
                    //更新切换有效期之后的价格
                    this.value.true_price=success.data.true_price
                    this.$emit('change_status')
                }).catch(error=>{
                    this.$message.error(error.success)
                })
            },
            //删除购物车
            del(){
                let token = localStorage.user_token || sessionStorage.user_token
                this.$axios({
                    url:this.$settings.HOST+'shoppingcart/option/',
                    method:'delete',
                    data:{
                       course_id:this.value.id
                    },
                    headers:{
                        //请求头中声明token
                        'Authorization': 'jwt '+token
                    }
                }).then(success=>{
                    this.$message.success(success.data.message)
                    //成功删除后调用父组件的方法从新计算中价格
                    this.$emit('del')
                }).catch(error=>{
                    this.$message.error(error.success)
                })


            },
            //改变复选框状态并保存redis
            change_status(){
                let token = localStorage.user_token || sessionStorage.user_token
                this.$axios.patch(`${this.$settings.HOST}shoppingcart/option/`,{
                    selected:this.value.selected,
                    course_id:this.value.id,
                },{
                    headers:{
                        //请求头中声明token
                            'Authorization': 'jwt '+token
                    }
                }).then(success=>{
                    this.$message.success(success.data.message)
                    this.$emit('change_status')
                }).catch(error=>{
                    this.$message.error(error.success)
                })
            },
        },
        data(){
            return{
                expire_time:'30天',


            }
        }
    }
</script>

<style scoped>
    .cart_item::after {
        content: "";
        display: block;
        clear: both;
    }

    .cart_column {
        float: left;
        height: 250px;
    }

    .cart_item .column_1 {
        width: 88px;
        position: relative;
    }

    .my_el_checkbox {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        top: 0;
        margin: auto;
        width: 16px;
        height: 16px;
    }

    .cart_item .column_2 {
        padding: 67px 10px;
        width: 520px;
        height: 116px;
    }

    .cart_item .column_2 img {
        width: 175px;
        height: 115px;
        margin-right: 35px;
        vertical-align: middle;
    }

    .cart_item .column_3 {
        width: 197px;
        position: relative;
        padding-left: 10px;
    }

    .my_el_select {
        width: 117px;
        height: 28px;
        position: absolute;
        top: 0;
        bottom: 0;
        margin: auto;
    }

    .cart_item .column_4 {
        padding: 67px 10px;
        height: 116px;
        width: 142px;
        line-height: 116px;
    }

</style>
