<template>
    <div>
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item label="监控时长(秒)">
            <el-input v-model="formInline.duration" placeholder="监控时长(秒)"></el-input>
        </el-form-item>
        <el-form-item label="监控频率(秒/次)">
            <el-input v-model="formInline.frequency" placeholder="监控频率(秒/次)"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary">开始监控</el-button>
        </el-form-item>
        </el-form>
        <br/>
    <div style="width:150px; height:22px;
              margin-left:0;margin-right:5%; margin-bottom: 0px; margin-top: 0px">
  <el-button type="primary" @click="showEnable=true">添加<i class="el-icon-upload el-icon--right"></i></el-button>
  </div>
  <br/>
    <el-table
    :data="tableData"
     @selection-change="handleSelectionChange">
    style="width: 100%">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      label="服务器ip"
      prop="ip">
    </el-table-column>
    <el-table-column
      label="服务器监控端口"
      prop="port">
    </el-table-column>
    <el-table-column
      label="监控状态"
      prop="state">
    </el-table-column>
    <el-table-column
      label="进程列表"
      prop="processList">
    </el-table-column>
    <el-table-column
      align="right">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  <br/>
  <el-dialog title="添加服务器" :visible.sync="showEnable">
  <el-form :model="form">
    <el-form-item label="服务器ip" :label-width="formLabelWidth">
      <el-input v-model="form.ip" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="服务器账号" :label-width="formLabelWidth">
      <el-input v-model="form.account" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="服务器密码" :label-width="formLabelWidth">
      <el-input v-model="form.password" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="监控端口" :label-width="formLabelWidth">
      <el-input v-model="form.port" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="监控进程列表" :label-width="formLabelWidth">
      <el-input v-model="form.processList" autocomplete="off"></el-input>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="showEnable = false">取 消</el-button>
    <el-button type="primary" @click="update()">确 定</el-button>
  </div>
</el-dialog>
</div>
</template>

<script>
import axios from 'axios'
  export default {
    data() {
      return {
          formInline: {
          duration: '',
          frequency: ''
        },
        showEnable: false,
        tableData: [{
          ip: '172.31.10.8',
          port: '9999',
          state: '正常',
          processList: '1067'
        }],
        search: '',
        form: {
          ip: '',
          account: '',
          password: '',
          port: '',
          processList: '',
        },
        formLabelWidth: '120px'
      }
    },
    methods: {
      handleEdit(index, row) {
        this.form=row
        this.showEnable=true
      },
      handleDelete(index) {
        this.tableData.splice(index,1)
      },
       handleSelectionChange(val) {
        this.multipleSelection = val;
      },
      update(){
        axios({
            url : 'http://127.0.0.1:8000/api/testapi/',
            method : 'post',
            data : this.form,
        }).then((response)=>{
            console.log(response.data)
            if(response.data=='True'){
                this.tableData.push({
                ip: this.form.ip,
                port: this.form.port,
                state: '正常',
                processList: this.form.processList
                })
            }
        })
        this.showEnable=false
      }
    },
  }
</script>